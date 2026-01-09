"""
Data Processing Module

Contains data generation and feature engineering utilities for fraud detection.
"""

from .feature_engineering import AdvancedFeatureEngineering
from .generate_data import (
    FraudDatasetGenerator,
    DatasetConfig,
    generate_and_save_data
)

__all__ = [
    "FraudDatasetGenerator",
    "DatasetConfig",
    "generate_and_save_data",
    "AdvancedFeatureEngineering"
]

__version__ = "1.0.0"
