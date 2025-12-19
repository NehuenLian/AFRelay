from zeep.helpers import serialize_object

from service.utils.logger import logger


def convert_zeep_object_to_dict(returned_xml: object) -> dict:

    """
    Zeep usually returns an object of type '<class 'zeep.objects.[service response]'>'.
    To work with the returned data, this object needs to be converted into a dictionary.
    This function performs that conversion and saves the data as a JSON file.
    """

    # Convert to dict/OrderedDict
    serialized_xml = serialize_object(returned_xml)
    logger.debug("Zeep object converted to dict.")

    return serialized_xml


def convert_pydantic_model_to_dict(sale_data: object) -> dict:
    # Convert pydantic model object to dict
    parsed_data = sale_data.model_dump()
    return parsed_data