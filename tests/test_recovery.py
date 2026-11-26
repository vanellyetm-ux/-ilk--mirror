import unittest
from tempfile import TemporaryDirectory
from pathlib import Path
from anchor.voe.recovery import evaluate

class RecoveryTests(unittest.TestCase):
    def check_state(self, status, action):
        with TemporaryDirectory() as d:
            r = evaluate(b'Voe payload', status, True, d)
            self.assertEqual(r['http_status'], status)
            self.assertEqual(r['action'], action)
            self.assertFalse(r['write_accepted'])
            self.assertEqual(Path(r['preserved_path']).read_bytes(), b'Voe payload')
    def test_verified(self):
        with TemporaryDirectory() as d:
            self.assertTrue(evaluate(b'x',201,True,d,'a'*40,b'x','a'*40)['write_accepted'])
    def test_mismatch(self):
        with TemporaryDirectory() as d:
            self.assertFalse(evaluate(b'x',201,True,d,'a'*40,b'y','a'*40)['write_accepted'])
    def test_unauthorized(self):
        with TemporaryDirectory() as d:
            self.assertFalse(evaluate(b'x',201,False,d,'a'*40,b'x','a'*40)['write_accepted'])

for status, action in [(401,'REAUTHENTICATE'),(403,'RESTORE_WRITE_PERMISSION'),(404,'VERIFY_REPOSITORY_AND_REF'),(409,'RECONCILE_CONFLICT'),(422,'VALIDATE_PAYLOAD'),(429,'RESPECT_RETRY_DELAY'),(500,'CONTROLLED_RETRY'),(503,'WAIT_FOR_SERVICE')]:
    setattr(RecoveryTests, f'test_{status}', lambda self,s=status,a=action:self.check_state(s,a))
