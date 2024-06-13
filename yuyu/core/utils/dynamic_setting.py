import json

from yuyu.core.models import DynamicSetting

BILLING_ENABLED = "billing_enabled"
INVOICE_TAX = "invoice_tax"
COMPANY_NAME = "company_name"
COMPANY_LOGO = "company_logo"
COMPANY_ADDRESS = "company_address"
EMAIL_ADMIN = "email_admin"
INVOICE_AUTO_DEDUCT_BALANCE = "invoice_auto_deduct_balance"
HOW_TO_TOP_UP = "how_to_top_up"

DEFAULTS = {
    BILLING_ENABLED: False,
    INVOICE_TAX: 11,
    COMPANY_NAME: "BTECH DEV",
    COMPANY_LOGO: '',
    COMPANY_ADDRESS: '',
    EMAIL_ADMIN: '',
    INVOICE_AUTO_DEDUCT_BALANCE: True,
    HOW_TO_TOP_UP: 'Please Contact Administrator'
}


def _get_casted_value(setting: DynamicSetting):
    if setting.type == DynamicSetting.DataType.JSON:
        return json.loads(setting.value)
    elif setting.type == DynamicSetting.DataType.BOOLEAN:
        return setting.value == "1"
    elif setting.type == DynamicSetting.DataType.INT:
        return int(setting.value)
    elif setting.type == DynamicSetting.DataType.STR:
        return setting.value
    else:
        raise ValueError("Type not supported")


def get_dynamic_settings():
    result = DEFAULTS.copy()
    settings = DynamicSetting.objects.all()
    for setting in settings:
        result[setting.key] = _get_casted_value(setting)

    return result


def get_dynamic_setting(key):
    setting: DynamicSetting = DynamicSetting.objects.filter(key=key).first()
    if not setting:
        return DEFAULTS[key]

    return setting.value


def set_dynamic_setting(key, value):
    if type(value) is dict:
        inserted_value = json.dumps(value)
        data_type = DynamicSetting.DataType.JSON
    elif type(value) is bool:
        inserted_value = "1" if value else "0"
        data_type = DynamicSetting.DataType.BOOLEAN
    elif type(value) is int:
        inserted_value = str(value)
        data_type = DynamicSetting.DataType.INT
    elif type(value) is str:
        inserted_value = value
        data_type = DynamicSetting.DataType.STR
    else:
        print("SETTING TAB = ", type(value))
        raise ValueError("Type not supported")

    DynamicSetting.objects.update_or_create(key=key, defaults={
        "value": inserted_value,
        "type": data_type
    })
