"""Run the reproducible platform hypothesis report."""
import logging
import sys
from pathlib import Path

from src.hypothesis_validation import (
    acute_window_difference,
    h4_moderation_regression,
    load_feature_data,
    platform_difference,
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Path(__file__).parent / 'logs' / 'main.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    logger.info("Loading engineered feature data...")
    data = load_feature_data()
    h1 = platform_difference(data, "fk_grade")
    h2 = platform_difference(data, "rigor_score")
    h3 = acute_window_difference(data, platform="Reddit")
    h4 = h4_moderation_regression(data)

    print("Echo of Anonymity hypothesis report")
    print(f"H1 lexical complexity: p={h1['p_value']:.3g}, Cliff's delta={h1['cliffs_delta']:.3f}")
    print(f"H2 evidentiary rigor: p={h2['p_value']:.3g}, Cliff's delta={h2['cliffs_delta']:.3f}")
    print(f"H3 Reddit acute intensity: p={h3['p_value']:.3g}, difference={h3['difference']:.3f}")
    print(f"H4 readability moderation: p={h4['interaction_p_value']:.3g}, R2={h4['r_squared']:.3f}")
    logger.info("Analysis complete")
    return 0

if __name__ == "__main__":
    sys.exit(main())
