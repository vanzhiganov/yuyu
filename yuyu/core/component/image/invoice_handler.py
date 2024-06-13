from yuyu.core.component.base.invoice_handler import InvoiceHandler
from yuyu.core.exception import PriceNotFound
from yuyu.core.models import PriceMixin, InvoiceImage, ImagePrice


class ImageInvoiceHandler(InvoiceHandler):
    INVOICE_CLASS = InvoiceImage
    KEY_FIELD = "image_id"
    PRICE_DEPENDENCY_FIELDS = ["space_allocation_gb"]
    INFORMATIVE_FIELDS = ["name"]

    def get_price(self, payload) -> PriceMixin:
        price = ImagePrice.objects.first()
        if price is None:
            raise PriceNotFound(identifier='image')

        return price
