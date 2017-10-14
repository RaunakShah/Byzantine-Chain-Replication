# -*- generated by 1.0.9 -*-
import da
PatternExpr_218 = da.pat.TuplePattern([da.pat.ConstantPattern('operation_result'), da.pat.FreePattern('returned_request_id'), da.pat.FreePattern('response'), da.pat.FreePattern('result_proof'), da.pat.FreePattern(None)])
PatternExpr_230 = da.pat.BoundPattern('_BoundPattern237_')
PatternExpr_339 = da.pat.TuplePattern([da.pat.BoundPattern('_BoundPattern340_'), da.pat.BoundPattern('_BoundPattern342_'), da.pat.BoundPattern('_BoundPattern344_')])
PatternExpr_347 = da.pat.BoundPattern('_BoundPattern349_')
PatternExpr_397 = da.pat.BoundPattern('_BoundPattern398_')
PatternExpr_400 = da.pat.BoundPattern('_BoundPattern401_')
PatternExpr_350 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern356_')]), da.pat.TuplePattern([da.pat.BoundPattern('_BoundPattern358_'), da.pat.BoundPattern('_BoundPattern359_'), da.pat.BoundPattern('_BoundPattern360_')])])
PatternExpr_402 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern408_')]), da.pat.BoundPattern('_BoundPattern409_')])
_config_object = {}

class Client(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._ClientReceivedEvent_0 = []
        self._ClientReceivedEvent_1 = []
        self._ClientReceivedEvent_2 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_0', PatternExpr_218, sources=[PatternExpr_230], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_1', PatternExpr_339, sources=[PatternExpr_347], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_ClientReceivedEvent_2', PatternExpr_397, sources=[PatternExpr_400], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, client_id, chain, workload, client_timeout, failures, public_key_list, **rest_412):
        super().setup(client_id=client_id, chain=chain, workload=workload, client_timeout=client_timeout, failures=failures, public_key_list=public_key_list, **rest_412)
        self._state.client_id = client_id
        self._state.chain = chain
        self._state.workload = workload
        self._state.client_timeout = client_timeout
        self._state.failures = failures
        self._state.public_key_list = public_key_list
        pass

    def run(self):
        workload_id = 0
        for request in self._state.workload:
            request_type = 'new'
            request_id = (self._state.client_id, workload_id)
            print('NEW ERQUEST')
            print(request)
            print(request_id)
            self.send(('operation_request', request_id, request_type, request, self._id), to=self._state.chain[0])
            super()._label('_st_label_215', block=False)
            result_proof = response = returned_request_id = None

            def ExistentialOpExpr_216():
                nonlocal result_proof, response, returned_request_id
                for (_, (_, _, _BoundPattern244_), (_ConstantPattern251_, returned_request_id, response, result_proof, _)) in self._ClientReceivedEvent_0:
                    if (_BoundPattern244_ == self._state.chain[(len(self._state.chain) - 1)]):
                        if (_ConstantPattern251_ == 'operation_result'):
                            if (returned_request_id == request_id):
                                return True
                return False
            _st_label_215 = 0
            self._timer_start()
            while (_st_label_215 == 0):
                _st_label_215 += 1
                if ExistentialOpExpr_216():
                    print(result_proof)
                    workload_id += 1
                    _st_label_215 += 1
                elif self._timer_expired:
                    print('Done')
                    _st_label_215 += 1
                else:
                    super()._label('_st_label_215', block=True, timeout=self._state.client_timeout)
                    _st_label_215 -= 1
            else:
                if (_st_label_215 != 2):
                    continue
            if (_st_label_215 != 2):
                break

    def verify(self, response):
        for result_statement_hash in response.result_proof:
            if (not (hash(result) == result_statement_hash)):
                reconfiguration_reqeust.proof_of_misbehavior = (result, result_proof)
                self.send(reconfiguration_request, to=Olympus)
                return false
        return true

    def retransmit(self, op_id, operation, replicas_in_config):
        request_type = 'retransmission'
        request_id = op_id
        retransmit_request = operation
        self.send((request_id, retransmit_request, request_type, self._id), to=replicas_in_config)
        super()._label('_st_label_336', block=False)
        _st_label_336 = 0
        while (_st_label_336 == 0):
            _st_label_336 += 1
            if PatternExpr_350.match_iter(self._ClientReceivedEvent_1, _BoundPattern356_=_, _BoundPattern358_=request_id, _BoundPattern359_=response, _BoundPattern360_=response_type, SELF_ID=self._id):
                _st_label_336 += 1
            else:
                super()._label('_st_label_336', block=True)
                _st_label_336 -= 1
        if (response_type == 'result'):
            self.verify(response)
        elif (response_type == 'error'):
            self._state.chain = self.getConfig(Olympus)
            self.retransmit(id, retransmit_request, self._state.chain.replicas)

    def getConfig(self, Olympus):
        self.send('configQuery', to=Olympus)
        super()._label('_st_label_394', block=False)
        _st_label_394 = 0
        while (_st_label_394 == 0):
            _st_label_394 += 1
            if PatternExpr_402.match_iter(self._ClientReceivedEvent_2, _BoundPattern408_=Olympus, _BoundPattern409_=self._state.chain, SELF_ID=self._id):
                _st_label_394 += 1
            else:
                super()._label('_st_label_394', block=True)
                _st_label_394 -= 1
        return self._state.chain