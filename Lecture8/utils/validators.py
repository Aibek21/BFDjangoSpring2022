from rest_framework import serializers


def num_pages_range_validation(value):
    if not (1 <= value <= 1000):
        raise serializers.ValidationError('Invalid num pages value')
