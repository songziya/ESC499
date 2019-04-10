# This file is part of tf-rddlsim.

# tf-rddlsim is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# tf-rddlsim is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with tf-rddlsim. If not, see <http://www.gnu.org/licenses/>.


from tfrddlsim.viz.abstract_visualizer import Visualizer
from tfrddlsim.viz.generic_visualizer import GenericVisualizer
from tfrddlsim.viz.navigation_visualizer import NavigationVisualizer
from tfrddlsim.viz.navigationv2_visualizer import Navigationv2Visualizer
from tfrddlsim.viz.navigationv3_visualizer import Navigationv3Visualizer
from tfrddlsim.viz.reservoir_visualizer import ReservoirVisualizer
from tfrddlsim.viz.bacteria_visualizer import BacteriaVisualizer
from tfrddlsim.viz.hvac_visualizer import HvacVisualizer
from tfrddlsim.viz.reward_visualizer import RewardVisualizer

visualizers = {
    'generic': GenericVisualizer,
    'navigation': NavigationVisualizer,
    'navigationv2': Navigationv2Visualizer,
    'navigationv3': Navigationv3Visualizer,
    'reservoir': ReservoirVisualizer,
    'bacteria': BacteriaVisualizer,
    'hvac': HvacVisualizer,
    'reward': RewardVisualizer
}
