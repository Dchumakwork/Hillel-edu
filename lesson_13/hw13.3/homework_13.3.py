import logging
import xml.etree.ElementTree as ET

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ф-я приймає номер групи і повертає та логує для неї значення "incoming" (при наявності) із файлу 'groups.xml'
def incom_search(group_number: int):
    incoming_requested = ''
    try:
        tree = ET.parse('groups.xml')
        root = tree.getroot()
        no_result = True
        for group in root.findall("group"):
            number = int(group.find("number").text)
            if group_number == number:
                no_result = False
                timing_exbytes = group.find('timingExbytes')
                if timing_exbytes is not None:
                    incoming = timing_exbytes.find('incoming')
                    if incoming is not None:
                        incoming_requested = incoming.text
                        logger.info(f'"Incoming" for {group_number} group is "{incoming.text}"')
                        print(f'Incoming for {group_number} group is "{incoming.text}"')
                        break
                    else:
                        logger.info(f'No incoming for {group_number} group')
                        print(f'No incoming for {group_number} group')
                else:
                    print(f'No timing_exbytes/incoming for {group_number} group')
                    logger.info(f'No timing_exbytes/incoming for {group_number} group')
        if no_result:
            logger.info(f'No {group_number} group in file')
            print(f'No {group_number} group in file')
    except ET.ParseError as e:
        logger.error(f"Parsing error for 'groups.xml': {e}")
        print(f"Parsing error for 'groups.xml': {e}")
    except Exception as e:
        logger.error(f"Some error during working with 'groups.xml': {e}")
        print(f"Some error during working with 'groups.xml': {e}")
    return incoming_requested

incom_search(0)
incom_search(1)
incom_search(10)
