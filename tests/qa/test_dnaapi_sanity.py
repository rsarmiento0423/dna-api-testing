import logging
import pytest
from tests.utils.comm_libs import BASE_URL, RP_PATH, AA_PATH, call_post_api

logger = logging.getLogger(__name__)

RP_ENDPOINT = BASE_URL + RP_PATH
AA_ENDPOINT = BASE_URL + AA_PATH

@pytest.mark.sanity
@pytest.mark.parametrize(
    "expected_result",
    [
        {
            "id": "790dcf38-81e7-5a89-8b1d-fde5b70b4271",
            "downtime_avg_days": 1.76,
            "downtime_stdev_days": 1.91,
            "score": "low",
        }
    ],
)
def test_return_period_integrated(expected_result):
    """Staging qa test for return period"""
    logger.info("Start staging qa test for return period1")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "integrated",
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    json_resp = call_post_api(url=RP_ENDPOINT, payload=data)
    assert (
        json_resp == expected_result
    ), f"Got the result: {json_resp}. It is not expected."
    logger.info("Finished staging qa test for return period1")

@pytest.mark.sanity
@pytest.mark.parametrize(
    "expected_result",
    [
        {
            "id": "790dcf38-81e7-5a89-8b1d-fde5b70b4271",
            "downtime_avg_days": 0.0,
            "downtime_stdev_days": 0.0,
            "score": "low",
        }
    ],
)
def test_return_period_utility(expected_result):
    """Staging qa test for return period"""
    logger.info("Start staging qa test for return period1")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "utility",
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    json_resp = call_post_api(url=RP_ENDPOINT, payload=data)
    assert (
        json_resp == expected_result
    ), f"Got the result: {json_resp}. It is not expected."
    logger.info("Finished staging qa test for return period1")

@pytest.mark.sanity
@pytest.mark.parametrize(
    "expected_result",
    [
        {
            "id": "790dcf38-81e7-5a89-8b1d-fde5b70b4271",
            "downtime_avg_days": 14.91,
            "downtime_stdev_days": 18.56,
            "score": "high",
        }
    ],
)
def test_return_period_community(expected_result):
    """Staging qa test for return period"""
    logger.info("Start staging qa test for return period1")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "community",
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    json_resp = call_post_api(url=RP_ENDPOINT, payload=data)
    assert (
        json_resp == expected_result
    ), f"Got the result: {json_resp}. It is not expected."
    logger.info("Finished staging qa test for return period1")

@pytest.mark.sanity
@pytest.mark.parametrize(
    "expected_result",
    [
        {
            "id": "790dcf38-81e7-5a89-8b1d-fde5b70b4271",
            "downtime_avg_days": 1.71,
            "downtime_stdev_days": 0.92,
            "score": "low",
        }
    ],
)
def test_return_period_ingres_egress(expected_result):
    """Staging qa test for return period"""
    logger.info("Start staging qa test for return period1")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "ingress_egress",
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    json_resp = call_post_api(url=RP_ENDPOINT, payload=data)
    assert (
        json_resp == expected_result
    ), f"Got the result: {json_resp}. It is not expected."
    logger.info("Finished staging qa test for return period1")

@pytest.mark.sanity
@pytest.mark.parametrize(
    "expected_result",
    [
        {
            "id": "790dcf38-81e7-5a89-8b1d-fde5b70b4271",
            "downtime_avg_days": 0.52,
            "downtime_stdev_days": 2.2,
            "score": "low",
        }
    ],
)
def test_return_period_repair_time(expected_result):
    """Staging qa test for return period2"""
    logger.info("Start staging qa test for return period")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "repair_time",
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    json_resp = call_post_api(url=RP_ENDPOINT, payload=data)
    assert (
        json_resp == expected_result
    ), f"Got the result: {json_resp}. It is not expected."
    logger.info("Finished staging qa test for return period2")

@pytest.mark.sanity
def test_return_period_typo_repair_time():
    """Staging qa test for typo repair_time in return_perion"""
    logger.info("Start staging qa test for return period3")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "repairtime",
        "climate_change": "cc2050_45",
        "return_period_yrs": 250,
        "peril": "flood",
    }
    call_post_api(url=RP_ENDPOINT, payload=data, expect_status_code=422)
    logger.info("Finished staging qa test for return period3")

@pytest.mark.sanity
@pytest.mark.parametrize(
    "expected_result",
    [
        {
            "id": "790dcf38-81e7-5a89-8b1d-fde5b70b4271",
            "downtime_avg_days": 0.02,
            "downtime_stdev_days": 0.07,
            "score": "low",
        }
    ],
)
def test_average_annual_integrated(expected_result):
    """Staging qa test for average annual"""
    logger.info("Start staging qa test for average annual1")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "integrated",
        "climate_change": "cc2050_45",
        "peril": "flood",
    }
    json_resp = call_post_api(url=AA_ENDPOINT, payload=data)
    assert (
        json_resp == expected_result
    ), f"Got the result: {json_resp}. It is not expected."
    logger.info("Finish staging qa test for average annual1")

@pytest.mark.sanity
@pytest.mark.parametrize(
    "expected_result",
    [
        {
            "id": "790dcf38-81e7-5a89-8b1d-fde5b70b4271",
            "downtime_avg_days": 0.0,
            "downtime_stdev_days": 0.04,
            "score": "low",
        }
    ],
)
def test_average_annual_utility(expected_result):
    """Staging qa test for average annual2"""
    logger.info("Start staging qa test for average annual2")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "utility",
        "climate_change": "cc2050_45",
        "peril": "flood",
    }
    json_resp = call_post_api(url=AA_ENDPOINT, payload=data)
    assert (
        json_resp == expected_result
    ), f"Got the result: {json_resp}. It is not expected."
    logger.info("Finish staging qa test for average annual2")

@pytest.mark.sanity
@pytest.mark.parametrize(
    "expected_result",
    [
        {
            "id": "790dcf38-81e7-5a89-8b1d-fde5b70b4271",
            "downtime_avg_days": 0.13,
            "downtime_stdev_days": 0.3,
            "score": "low",
        }
    ],
)
def test_average_annual_community(expected_result):
    """Staging qa test for average annual2"""
    logger.info("Start staging qa test for average annual2")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "community",
        "climate_change": "cc2050_45",
        "peril": "flood",
    }
    json_resp = call_post_api(url=AA_ENDPOINT, payload=data)
    assert (
        json_resp == expected_result
    ), f"Got the result: {json_resp}. It is not expected."
    logger.info("Finish staging qa test for average annual2")

@pytest.mark.sanity
@pytest.mark.parametrize(
    "expected_result",
    [
        {
            "id": "790dcf38-81e7-5a89-8b1d-fde5b70b4271",
            "downtime_avg_days": 0.02,
            "downtime_stdev_days": 0.2,
            "score": "low",
        }
    ],
)
def test_average_annual_ingress_egress(expected_result):
    """Staging qa test for average annual2"""
    logger.info("Start staging qa test for average annual2")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "ingress_egress",
        "climate_change": "cc2050_45",
        "peril": "flood",
    }
    json_resp = call_post_api(url=AA_ENDPOINT, payload=data)
    assert (
        json_resp == expected_result
    ), f"Got the result: {json_resp}. It is not expected."
    logger.info("Finish staging qa test for average annual2")

@pytest.mark.sanity
@pytest.mark.parametrize(
    "expected_result",
    [
        {
            "id": "790dcf38-81e7-5a89-8b1d-fde5b70b4271",
            "downtime_avg_days": 0.01,
            "downtime_stdev_days": 0.31,
            "score": "low",
        }
    ],
)
def test_average_annual_repair_time(expected_result):
    """Staging qa test for average annual2"""
    logger.info("Start staging qa test for average annual2")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "repair_time",
        "climate_change": "cc2050_45",
        "peril": "flood",
    }
    json_resp = call_post_api(url=AA_ENDPOINT, payload=data)
    assert (
        json_resp == expected_result
    ), f"Got the result: {json_resp}. It is not expected."
    logger.info("Finish staging qa test for average annual2")

@pytest.mark.sanity
def test_average_annual_typo_repair_time():
    """Staging qa test for typo repair_time for average annual"""
    logger.info("Start staging qa test for average annual3")
    data = {
        "latitude": 33.814437,
        "longitude": -118.051187,
        "max_distance_m": 500,
        "interruption_type": "repairtime",
        "climate_change": "cc2050_45",
        "peril": "flood",
    }
    call_post_api(url=AA_ENDPOINT, payload=data, expect_status_code=422)
    logger.info("Finish staging qa test for average annual3")
