import pytest

from src.design import DesignModule
from src.planning import PlanningModule
from src.vision import VisionModule
from src.control import ControlModule
from src.monitoring import MonitoringModule
from src.adaptation import AdaptationModule
from src.interfaces import InterfaceModule

def test_module_imports():
    assert DesignModule is not None
    assert PlanningModule is not None
    assert VisionModule is not None
    assert ControlModule is not None
    assert MonitoringModule is not None
    assert AdaptationModule is not None
    assert InterfaceModule is not None 