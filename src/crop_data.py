from constants import (
    GRAPE,
    ENTER_CROP_TYPE_MESSAGE,
    ENTER_WIDTH_MESSAGE,
    ENTER_LENGTH_MESSAGE,
    ENTER_INPUT_TYPE_MESSAGE,
    ENTER_INPUT_DOSAGE_MESSAGE,
    ENTER_ROW_SPACING_MESSAGE
)

def create_record():
    crop_type = input(ENTER_CROP_TYPE_MESSAGE).strip().lower()
    width_meters = float(input(ENTER_WIDTH_MESSAGE))
    length_meters = float(input(ENTER_LENGTH_MESSAGE))
    input_type = input(ENTER_INPUT_TYPE_MESSAGE).strip().lower()
    input_dosage = float(input(ENTER_INPUT_DOSAGE_MESSAGE))

    row_spacing_meters = None

    if crop_type == GRAPE:
        row_spacing_meters = float(input(ENTER_ROW_SPACING_MESSAGE))

    record = [
        crop_type,
        width_meters,
        length_meters,
        None,
        input_type,
        input_dosage,
        None,
        row_spacing_meters,
        None,
        None
    ]

    return record