from unittest.mock import sentinel

from mhs_common import workflow
import unittest


class TestWorkflow(unittest.TestCase):
    def test_get_workflow_map_for_outbound(self):
        workflow_map = workflow.get_workflow_map(party_key=sentinel.party_key, persistence_store=sentinel.persistence_store, transmission=sentinel.transmission)
        self.check_workflows_are_present(workflow_map)

    def test_get_workflow_map_for_inbound(self):
        workflow_map = workflow.get_workflow_map(queue_adaptor=sentinel.queue_adaptor)
        self.check_workflows_are_present(workflow_map)

    def check_workflows_are_present(self, workflow_map):
        workflow_names = [workflow.SYNC, workflow.ASYNC_EXPRESS, workflow.ASYNC_RELIABLE, workflow.FORWARD_RELIABLE]
        for workflow_name in workflow_names:
            self.assertIn(workflow_name, workflow_map)
