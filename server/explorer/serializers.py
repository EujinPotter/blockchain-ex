from .models import *
from rest_framework import serializers


class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = ('commitment', 'height')


class OutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Output
        fields = ('commitment',)


class KernelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kernel
        fields = ('block_id', 'fee', 'kernel_id', 'minHeight', 'maxHeight')


class BlockPaginatorSerializer(serializers.ModelSerializer):
    inputs = serializers.SerializerMethodField()
    outputs = serializers.SerializerMethodField()
    kernels = serializers.SerializerMethodField()

    def get_inputs(self, obj):
        return obj.inputs.count()

    def get_outputs(self, obj):
        return obj.outputs.count()

    def get_kernels(self, obj):
        return obj.kernels.count()

    class Meta:
        model = Block
        fields = ('height', 'hash',
                  'difficulty', 'timestamp',
                  'fee', 'inputs', 'outputs', 'kernels')


class BlockSerializer(serializers.ModelSerializer):

    inputs = serializers.SerializerMethodField()
    outputs = serializers.SerializerMethodField()
    kernels = serializers.SerializerMethodField()

    def get_inputs(self, obj):
        qs = obj.inputs.all()
        return InputSerializer(qs, many=True, read_only=True).data

    def get_outputs(self, obj):
        qs = obj.outputs.all()
        return OutputSerializer(qs, many=True, read_only=True).data

    def get_kernels(self, obj):
        qs = obj.kernels.all()
        return KernelSerializer(qs, many=True, read_only=True).data

    class Meta:
        model = Block
        fields = ('height', 'prev', 'hash', 'chainwork', 'rate_btc', 'rate_usd',
                  'difficulty', 'subsidy', 'timestamp',
                  'fee', 'inputs', 'outputs', 'kernels')
                  

class ForkDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forks_event_detection
        fields = "__all__"


class BotUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bot_users
        fields = "__all__"


class MaxPrivacyWithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Max_privacy_withdraw
        fields = ('value', 'created_at')


class SwapStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swap_stats
        fields = ('btc', 'dash', 'doge', 'ltc', 'qtum', 'wbtc', 'tether', 'eth', 'dai')


class ContractCallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract_calls
        fields = ('height','cname','imethod','methodname','faction','fval')


class ContractFundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract_funds
        fields = ('aid','value')


class ContractFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('cid', 'height', 'name', 'sid', 'subtype')


class ContractSerializer(serializers.ModelSerializer):
    calls = serializers.SerializerMethodField()
    funds = serializers.SerializerMethodField()

    def get_calls(self, obj):
        qs = obj.calls.all()
        return ContractCallsSerializer(qs, many=True, read_only=True).data

    def get_funds(self, obj):
        qs = obj.funds.all()
        return ContractFundsSerializer(qs, many=True, read_only=True).data

    class Meta:
        model = Contract
        fields = ('cid', 'height', 'name', 'sid', 'subtype', 'calls', 'funds')
        