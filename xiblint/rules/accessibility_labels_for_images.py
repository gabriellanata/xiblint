from xiblint.rules import Rule
from xiblint.xibutils import (
    view_is_accessibility_element,
    view_accessibility_label,
    get_view_user_defined_attr,
)

if False:  # if TYPE_CHECKING:
    from xiblint.xibcontext import XibContext


class AccessibilityLabelsForImages(Rule):
    """
    Checks for accessible images with no accessibility label.
    In this case, VoiceOver will announce the image asset's name, which might be unwanted.
    """
    def check(self, context):  # type: (XibContext) -> None
        for image_view in context.tree.findall(".//imageView"):
            if (
                    view_is_accessibility_element(image_view) is True and
                    not view_accessibility_label(image_view) and
                    not get_view_user_defined_attr(image_view, 'accessibilityFormat')
            ):
                context.error(image_view, "Image is accessible but has no accessibility label")
