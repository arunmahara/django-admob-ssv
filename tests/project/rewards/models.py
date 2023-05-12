from django.db import models


class Reward(models.Model):
    """
    https://developers.google.com/admob/android/rewarded-video-ssv#ssv_callback_parameters
    """

    transaction_id = models.CharField(
        blank=True,
        max_length=256,
        help_text="Unique hex encoded identifier for each reward grant event generated by AdMob.",
    )

    timestamp = models.IntegerField(
        blank=True,
        help_text="Timestamp of when the user was rewarded as Epoch time in ms.",
    )

    ad_network = models.IntegerField(
        blank=True,
        null=True,
        help_text="Ad network identifier for the network that fulfilled this ad.",
    )

    ad_unit = models.IntegerField(
        blank=True,
        null=True,
        help_text="AdMob ad unit id that was used to request the rewarded video ad.",
    )

    reward_amount = models.PositiveIntegerField(
        # Maximum number is 2147483647 according to the Admob reward settings UI
        blank=True,
        help_text="Reward amount as specified in the ad unit settings.",
    )

    reward_item = models.CharField(
        blank=True,
        max_length=512,  # taken from the Admob reward settings UI
        help_text="Reward item as specified in the ad unit settings.",
    )

    user_id = models.CharField(
        blank=True,
        max_length=256,
        help_text="User identifier as provided by your app.",
    )

    custom_data = models.TextField(
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
