"""
This file defines class REINFORCE.

@author: Clemens Rosenbaum :: cgbr@cs.umass.edu
@created: 6/7/18
"""
import torch

from ..DecisionLayer import DecisionLayer


class REINFORCE(DecisionLayer):
    """
    Class REINFORCE defines ...
    """
    @staticmethod
    def _loss(sample):
        return - sample.state.log_prob(sample.action) * sample.cum_return

    def _forward(self, xs, mxs, agent):
        policy = self._policy[agent](xs)
        distribution = torch.distributions.Categorical(logits=policy)
        if (distribution.probs < 0.).any():
            print('less than 0.', distribution.probs)
        if torch.isnan(distribution.probs).any():
            print('not a num.  ', distribution.probs)
        actions = distribution.sample()
        return actions, distribution