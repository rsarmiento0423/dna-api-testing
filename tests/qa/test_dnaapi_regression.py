import logging
import pytest
from tests.utils.comm_libs import BASE_URL, RP_PATH, AA_PATH, call_post_api

logger = logging.getLogger(__name__)

RP_ENDPOINT = BASE_URL + RP_PATH
AA_ENDPOINT = BASE_URL + AA_PATH

@pytest.mark.regression
@pytest.mark.parametrize(
    "interruption_type, status",
    [
        ("community", 200),
        ("integrated", 200),
        ("ingress_egress", 200),
        ("utility", 200),
        ("repair_time", 200),
        ("", 422),
        ("Repair_time", 422),
        ("REPAIR_TIME", 422)
    ]
)
def test_interruption_type_return_period(interruption_type, status):
    data = {
        "interruption_type": interruption_type,
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    """QA testing for interruption_type on return_period endpoint"""
    logger.info("Start QA test for interruption_type on return_period endpoint")
    call_post_api(url=RP_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for interruption_type on return_period endpoint")

@pytest.mark.regression
@pytest.mark.parametrize(
    "climate_change,status",
    [
        ("cc2050_45", 200),
        ("ccbaseline", 200),
        ("", 422)
    ]
)
def test_climate_change_return_period(climate_change, status):
    """QA testing for climate_change on return_period endpoint"""
    logger.info("Start QA test for climate_change on return_period endpoint")
    data = {
        "interruption_type": "repair_time",
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "climate_change": climate_change,
        "return_period_yrs": 250,
        "peril": "flood",
    }
    call_post_api(url=RP_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for climate_change on return_period endpoint")

@pytest.mark.regression
@pytest.mark.parametrize(
    "peril,status",
    [
        ("flood", 200),
        ("seismic", 200),
        ("wind", 200),
        ("", 422)
    ]
)
def test_peril_return_period(peril, status):
    """QA testing for peril on return_period endpoint"""
    logger.info("Start QA test for peril on return_period endpoint")
    data = {
        "interruption_type": "repair_time",
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": peril,
    }
    call_post_api(url=RP_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for peril on return_period endpoint")

@pytest.mark.regression
@pytest.mark.parametrize(
    "max_distance_m,status",
    [
        ("0", 422),
        ("-1", 422),
        ("501", 422),
        ("500.0", 200),
        ("", 422)
    ]
)
def test_max_distance_m_return_period(max_distance_m, status):
    """QA testing for max_distance_m on return_period endpoint"""
    logger.info("Start QA test for max_distance_m on return_period endpoint")
    data = {
        "interruption_type": "repair_time",
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": max_distance_m,
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    call_post_api(url=RP_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for max_distance_m on return_period endpoint")

@pytest.mark.regression
@pytest.mark.parametrize(
    "latitude,status",
    [
        ("91", 422),
        ("-91", 422),
        ("", 422)
    ]
)
def test_latitude_return_period(latitude, status):
    """QA testing for latitude on return_period endpoint"""
    logger.info("Start QA test for latitude on return_period endpoint")
    data = {
        "interruption_type": "repair_time",
        "latitude": latitude,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    call_post_api(url=RP_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for latitude on return_period endpoint")

@pytest.mark.regression
@pytest.mark.parametrize(
    "longitude,status",
    [
        ("181", 422),
        ("-181", 422),
        ("", 422)
    ]
)
def test_longitude_return_period(longitude, status):
    """QA testing for longitude on return_period endpoint"""
    logger.info("Start QA test for longitude on return_period endpoint")
    data = {
        "interruption_type": "repair_time",
        "latitude": 33.814437,
        "longitude": longitude,
        "max_distance_m": 500,
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    call_post_api(url=RP_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for longitude on return_period endpoint")

@pytest.mark.regression
@pytest.mark.parametrize(
    "interruption_type, status",
    [
        ("community", 200),
        ("integrated", 200),
        ("ingress_egress", 200),
        ("utility", 200),
        ("repair_time", 200),
        ("", 422),
        ("Repair_time", 422),
        ("REPAIR_TIME", 422)
    ]
)
def test_interruption_type_average_annual(interruption_type, status):
    data = {
        "interruption_type": interruption_type,
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    """QA testing for interruption_type on average_annual endpoint"""
    logger.info("Start QA test for interruption_type on average_annual endpoint")
    call_post_api(url=AA_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for interruption_type on average_annual endpoint")

@pytest.mark.regression
@pytest.mark.parametrize(
    "climate_change,status",
    [
        ("cc2050_45", 200),
        ("ccbaseline", 200),
        ("", 422)
    ]
)
def test_climate_change_average_annual(climate_change, status):
    """QA testing for climate_change on average_annual endpoint"""
    logger.info("Start QA test for climate_change on average_annual endpoint")
    data = {
        "interruption_type": "repair_time",
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "climate_change": climate_change,
        "return_period_yrs": 250,
        "peril": "flood",
    }
    call_post_api(url=AA_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for climate_change on average_annual endpoint")

@pytest.mark.regression
@pytest.mark.parametrize(
    "peril,status",
    [
        ("flood", 200),
        ("seismic", 200),
        ("wind", 200),
        ("", 422)
    ]
)
def test_peril_average_annual(peril, status):
    """QA testing for peril on average_annual endpoint"""
    logger.info("Start QA test for peril on average_annual endpoint")
    data = {
        "interruption_type": "repair_time",
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": peril,
    }
    call_post_api(url=AA_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for peril on average_annual endpoint")

@pytest.mark.regression
@pytest.mark.parametrize(
    "max_distance_m,status",
    [
        ("0", 422),
        ("-1", 422),
        ("501", 422),
        ("500.0", 200),
        ("", 422)
    ]
)
def test_max_distance_m_average_annual(max_distance_m, status):
    """QA testing for max_distance_m on average_annual endpoint"""
    logger.info("Start QA test for max_distance_m on average_annual endpoint")
    data = {
        "interruption_type": "repair_time",
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": max_distance_m,
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    call_post_api(url=AA_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for max_distance_m on average_annual endpoint")

@pytest.mark.regression
@pytest.mark.parametrize(
    "latitude,status",
    [
        ("91", 422),
        ("-91", 422),
        ("", 422)
    ]
)
def test_latitude_average_annual(latitude, status):
    """QA testing for latitude on average_annual endpoint"""
    logger.info("Start QA test for latitude on average_annual endpoint")
    data = {
        "interruption_type": "repair_time",
        "latitude": latitude,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    call_post_api(url=AA_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for latitude on average_annual endpoint")

@pytest.mark.regression
@pytest.mark.parametrize(
    "longitude,status",
    [
        ("181", 422),
        ("-181", 422),
        ("", 422)
    ]
)
def test_longitude_average_annual(longitude, status):
    """QA testing for longitude on average_annual endpoint"""
    logger.info("Start QA test for longitude on average_annual endpoint")
    data = {
        "interruption_type": "repair_time",
        "latitude": 33.814437,
        "longitude": longitude,
        "max_distance_m": 500,
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    call_post_api(url=AA_ENDPOINT, payload=data, expect_status_code=status)
    logger.info("Finished QA test for longitude on average_annual endpoint")
