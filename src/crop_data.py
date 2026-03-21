from area_calculations import (
    calculate_rectangular_area,
    calculate_grape_row_count,
    calculate_total_row_length,
    calculate_grape_area
)
from input_calculations import (
    calculate_grape_input,
    calculate_corn_input
)
from constants import (
    GRAPE,
    CORN,
    ENTER_CROP_TYPE_MESSAGE,
    ENTER_WIDTH_MESSAGE,
    ENTER_LENGTH_MESSAGE,
    ENTER_INPUT_TYPE_MESSAGE,
    ENTER_ROW_WIDTH_MESSAGE,
    ENTER_GRAPE_INPUT_DOSAGE_MESSAGE,
    ENTER_CORN_INPUT_DOSAGE_MESSAGE
)

def create_record():
    crop_type = input(ENTER_CROP_TYPE_MESSAGE).strip().lower()
    width_meters = float(input(ENTER_WIDTH_MESSAGE))
    length_meters = float(input(ENTER_LENGTH_MESSAGE))
    input_type = input(ENTER_INPUT_TYPE_MESSAGE).strip().lower()

    if crop_type == GRAPE:
        input_dosage = float(input(ENTER_GRAPE_INPUT_DOSAGE_MESSAGE))
        row_spacing_meters = float(input(ENTER_ROW_WIDTH_MESSAGE))

        area = calculate_grape_area(width_meters, length_meters)
        row_count = calculate_grape_row_count(width_meters, row_spacing_meters)
        total_row_length = calculate_total_row_length(row_count, length_meters)
        total_input = calculate_grape_input(total_row_length, input_dosage)

        record = [
            crop_type,
            width_meters,
            length_meters,
            area,
            input_type,
            input_dosage,
            total_input,
            row_spacing_meters,
            row_count,
            total_row_length
        ]

        return record

    if crop_type == CORN:
        input_dosage = float(input(ENTER_CORN_INPUT_DOSAGE_MESSAGE))

        area = calculate_rectangular_area(width_meters, length_meters)
        total_input = calculate_corn_input(area, input_dosage)

        record = [
            crop_type,
            width_meters,
            length_meters,
            area,
            input_type,
            input_dosage,
            total_input,
            None,
            None,
            None
        ]

        return record

    print("Invalid crop type.")
    return None