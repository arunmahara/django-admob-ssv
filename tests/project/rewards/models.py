from django.db import models


class Reward(models.Model):
    """
    https://developers.google.com/admob/android/rewarded-video-ssv#ssv_callback_parameters
    """

    # This field should be unique. However, test callbacks always have the same transaction_id.
    # Therefore, we left it as non-unique to allow multiple test callbacks to be saved.
    transaction_id = models.CharField(
        max_length=256,
        help_text="Unique hex encoded identifier for each reward grant event generated by AdMob.",
    )

    timestamp = models.IntegerField(
        help_text="Timestamp of when the user was rewarded as Epoch time in ms.",
    )

    ad_network = models.IntegerField(
        help_text="Ad network identifier for the network that fulfilled this ad.",
    )

    ad_unit = models.IntegerField(
        help_text="AdMob ad unit id that was used to request the rewarded video ad.",
    )

    # Maximum number is 2147483647 according to the Admob reward settings UI
    reward_amount = models.PositiveIntegerField(
        help_text="Reward amount as specified in the ad unit settings.",
    )

    # The maximum length is taken from the Admob reward settings UI
    reward_item = models.CharField(
        max_length=512,
        help_text="Reward item as specified in the ad unit settings.",
    )

    # The max length is taken from the Admob reward settings UI
    user_id = models.CharField(
        max_length=256,
        blank=True,
        help_text="User identifier as provided by your app.",
    )

    # The max length is taken from the Admob reward settings UI
    custom_data = models.CharField(
        max_length=1024,
        blank=True,
        help_text="Custom data string as provided by your app.",
    )

    key_id = models.IntegerField(
        help_text="Key to be used to verify SSV callback.",
    )

    signature = models.CharField(
        max_length=512,
        help_text="Signature for SSV callback generated by AdMob.",
    )

    def __str__(self):
        return f"Reward #{self.pk}"
