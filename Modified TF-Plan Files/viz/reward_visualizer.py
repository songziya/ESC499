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
from rddl2tf.compiler import Compiler

import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

from typing import Sequence, Optional, Tuple, Union
Value = Union[bool, int, float, np.array]
NonFluents = Sequence[Tuple[str, Value]]
Fluents = Sequence[Tuple[str, np.array]]


class RewardVisualizer(Visualizer):
    '''
    Scott:
    Visualizer for the Reservoir domain.

    It uses Matplotlib.pyplot to render a graphical representation
    of the reservoirs' states, the initial and final states.

    Args:
        compiler (:obj:`rddl2tf.compiler.Compiler`): RDDL2TensorFlow compiler
        verbose (bool): Verbosity flag
    '''

    def __init__(self, compiler: Compiler, verbose: bool) -> None:
        super().__init__(compiler, verbose)

    def render(self,
            trajectories: Tuple[NonFluents, Fluents, Fluents, Fluents, np.array],
            batch: Optional[int] = None) -> None:
        '''Render the simulated state-action `trajectories` for Navigation domain.

        Args:
            stats: Performance statistics.
            trajectories: NonFluents, states, actions, interms and rewards.
            batch: Number of batches to render.
        '''

        non_fluents, initial_state, states, actions, interms, rewards = trajectories
        #print(initial_state)
        #print(type(initial_state))
        non_fluents = dict(non_fluents)
        
        states  = dict((name, fluent[0]) for name, fluent in states)
        #print(states)
        interms = dict((name, fluent[0]) for name, fluent in interms)
        
        actions = dict((name, fluent[0]) for name, fluent in actions)
        #print(actions)
        print(rewards)
        rewards = rewards[0]

        idx = self._compiler.state_fluent_ordering.index('temp/1')
        #print(idx)
        start = initial_state[idx][0]
        #print(initial_state[idx])
        #print(start)
        #print(start.shape)
        
        gup = non_fluents['TEMP_UP/1']
        glow = non_fluents['TEMP_LOW/1']
        #g = non_fluents['desired_temp/1']
        #print(g)
        
        path = states['temp/1']
        #print(path)
        #print(path.shape)

## select fluent to extract action from:        
        deltas = actions['air/1'] # v1, v3
        #deltas = interms['airbound/1'] # v2
        #print(deltas)
        #print(deltas.shape)
##        
        
        horizon = deltas.shape[0]
        res = deltas.shape[1]
        #print(res)
        
        self._ax1 = plt.gca()
        red_line = mlines.Line2D([],[], color='red', label='actions')
        blue_line = mlines.Line2D([],[], color='blue', label='state')
        lime_line = mlines.Line2D([0],[0], color ='w', markerfacecolor='limegreen', marker='X', markersize = 15, label='initial temperature')
        crim_line = mlines.Line2D([0],[0], color ='w', markerfacecolor='crimson', marker='X', markersize=15, label='desired temperature')
        plt.legend(handles=[red_line, blue_line, lime_line, crim_line])
        
        self._render_state_space(horizon)
        xpath = list(range(0,horizon+1))
        for i in range(0,res):
            self._render_start_and_goal_positions(start[i], gup[i], horizon)
            self._render_start_and_goal_positions(start[i], glow[i], horizon)
            ypath = [p[i] for p in path]
            ypath.insert(0, start[i])
            self._render_state_trajectory(xpath, ypath)
            yaction = [d[i] for d in deltas]
            yaction.append(0)
            self._render_action_trajectory(xpath, yaction)
            
        #self._render_start_and_goal_positions(start, g)
        #self._render_state_action_trajectory(start, path, deltas)

        plt.title('HVAC Control', fontweight='bold')
        #plt.legend(loc='lower right')
        plt.show()

    def _render_state_space(self, horizon):
        lower, upper = (-5.0, -5.0), (horizon+5.0, 55.0)
        self._ax1.axis([lower[0], upper[0], lower[1], upper[1]])
        self._ax1.set_aspect("auto")
        self._ax1.set_xlabel("horizon")
        self._ax1.set_ylabel("temperature")
        self._ax1.grid()

    def _render_start_and_goal_positions(self, start, goal, horizon):
        #print([start[0]])
        #print(start.shape)
        self._ax1.plot([0], [start], marker='X', markersize=10, color='limegreen', label='initial')
        self._ax1.plot([horizon], [goal], marker='X', markersize=10, color='crimson', label='goal')


    def _render_state_trajectory(self, xpath, ypath):
        # xpath = [ p[0] for p in path ]
        # ypath = [ p[1] for p in path ]
        #self._ax1.plot(xpath, ypath, 'b.', label='states')
        self._ax1.plot(xpath, ypath, 'b')
        # x0, y0 = start
        # xdeltas = [ d[0] for d in deltas ]
        # ydeltas = [ d[1] for d in deltas ]
        # self._ax1.quiver([x0] + xpath[:-1], [y0] + ypath[:-1], xdeltas, ydeltas,
        #     angles='xy', scale_units='xy', scale=1, color='dodgerblue', width=0.005,
        #     label='actions')
        
    def _render_action_trajectory(self, xaction, yaction):
        self._ax1.plot(xaction, yaction, 'r')
