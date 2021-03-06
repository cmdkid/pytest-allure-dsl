import pytest

from pytest_allure_dsl import InvalidInstruction, StepsWasNotUsed


def test_with_invalid_description_should_work_without_using_pytest_dsl():
    """
    invalid: yaml: description:
    """
    pass


def test_with_invalid_description_should_fail_if_using_pytest_dsl(allure_dsl):
    """
    steps:
        1: Hello World!
        2: invalid: yaml
    """
    with pytest.raises(InvalidInstruction):
        with allure_dsl.step(1):
            pass


@pytest.mark.xfail(raises=StepsWasNotUsed, strict=True)
def test_missed_step(allure_dsl, request):
    """
    steps:
        1: Hello,
        2: world!
    """
    with allure_dsl.step(1):
        pass
    request.node.allure_dsl._check_steps_was_used()


def test_dynamic_skip(allure_dsl):
    """
    steps:
        1: Hello,
        2: world!
    """
    with allure_dsl.step(1):
        pytest.skip('No more!')
    with allure_dsl.step(2):
        pass
