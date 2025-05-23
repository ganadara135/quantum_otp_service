from spinqit import (
    Circuit, H,
    get_compiler, get_basic_simulator, BasicSimulatorConfig
)
from random import choices

def generate_quantum_otp_decimal(digits: int = 6) -> str:
    n = max(3, digits)                 # 최소 3-qubit
    circ = Circuit()
    q = circ.allocateQubits(n)

    # Hadamard 게이트를 각 큐비트에 적용
    for qb in q:
        circ << (H, qb)                # ✅ Gate 클래스 그대로 사용

    # 컴파일 → 실행
    compiler = get_compiler("native")
    exe      = compiler.compile(circ, 0)

    backend  = get_basic_simulator()
    cfg      = BasicSimulatorConfig()
    cfg.configure_shots(1024)          # 1024번 측정해 분포 생성
    result   = backend.execute(exe, cfg)

    # 가중치(측정횟수)에 따라 무작위로 한 비트열 선택
    keys     = list(result.counts.keys())
    weights  = [result.counts[k] for k in keys]
    bitstr   = choices(keys, weights)[0]

    # return bitstr[:digits]             # 앞에서 원하는 자리수만
    return int(bitstr[:digits], 2)  # ← 십진수로 변환,  111111 -> 63






# # otp_quantum.py
# from spinqit import Circuit, H, get_compiler, get_basic_simulator, BasicSimulatorConfig

# def generate_quantum_otp(digits: int = 4) -> str:
#     n = max(3, digits)
#     circ = Circuit()
#     q    = circ.allocateQubits(n)
#     for i in range(n):
#         circ << (H, q[i])

#     engine   = get_basic_simulator()
#     compiler = get_compiler("native")
#     exe      = compiler.compile(circ, 0)

#     cfg = BasicSimulatorConfig()
#     cfg.configure_shots(1024)        # 1 shot에서 드물게 block 보고됨 → 1024 추천
#     result = engine.execute(exe, cfg)

#     bitstring = next(iter(result.counts))   # e.g. '11001'
#     return bitstring[:digits]






# from spinqit import (
#     Circuit,                 # 회로
#     H,                       # Hadamard 게이트
#     get_compiler,
#     get_basic_simulator,
#     BasicSimulatorConfig
# )

# def generate_quantum_otp(digits: int = 4) -> str:
#     n = max(3, digits)           # 최소 3-qubit
#     circ = Circuit()
#     q    = circ.allocateQubits(n)

#     # ❶ 모든 qubit을 |+> 상태로
#     for i in range(n):
#         circ << (H, q[i])

#     # ❷ 컴파일 & 실행
#     comp   = get_compiler("native")
#     engine = get_basic_simulator()
#     exe    = comp.compile(circ, 0)        # optimization_level = 0

#     cfg = BasicSimulatorConfig()
#     cfg.configure_shots(1)                # 한 번만 샷
#     result = engine.execute(exe, cfg)

#     bitstring = next(iter(result.counts)) # 예: '10110'
#     return bitstring[:digits]             # 앞에서 원하는 자리수만




# from spinqit import (
#     Circuit,                     # 회로 클래스
#     H, MEASURE,                  # 게이트
#     get_compiler,                # 컴파일러
#     get_basic_simulator,         # 백엔드
#     BasicSimulatorConfig         # 실행 설정
# )

# def generate_quantum_otp(digits: int = 4) -> str:
#     n = max(3, digits)           # 최소 3큐비트
#     circ = Circuit()
#     q = circ.allocateQubits(n)

#     # ❶ 게이트 배치
#     for i in range(n):
#         circ << (H, q[i])
#         circ << (MEASURE, q[i])

#     # ❷ 컴파일
#     comp   = get_compiler("native")      # 'native', 'ir' 등
#     exe    = comp.compile(circ, 0)       # optimisation_level = 0

#     # ❸ 시뮬레이터 실행
#     engine = get_basic_simulator()
#     cfg    = BasicSimulatorConfig()
#     cfg.configure_shots(1)               # 한 번만 측정
#     result = engine.execute(exe, cfg)    # ✨ 핵심: execute

#     bitstring = next(iter(result.counts))  # 예: '01101'
#     return bitstring[:digits]




# from spinqit import Circuit, get_basic_simulator, BasicSimulatorConfig
# from spinqit import H, MEASURE

# def generate_quantum_otp(digits=4):
#     qubit_count = max(3, digits)
#     circuit = Circuit()
#     q = circuit.allocateQubits(qubit_count)

#     for i in range(qubit_count):
#         circuit << (H, q[i])
#         circuit << (MEASURE, q[i])

#     sim = get_basic_simulator()
#     config = BasicSimulatorConfig()
#     result = sim.run(circuit, config)

#     counts = result.binary().split('\n')[0].strip()
#     return counts[:digits]



# from spinqit.model import Circuit
# from spinqit.model.gates import H, MEASURE
# from spinqit.sdk.executor import Executor
# from spinqit.sdk.backend import BasicSimulatorBackend

# def generate_quantum_otp(digits=4):
#     qubit_count = max(3, digits)
#     circuit = Circuit()
#     q = circuit.allocateQubits(qubit_count)

#     for i in range(qubit_count):
#         circuit.append(H(q[i]))
#         circuit.append(MEASURE(q[i]))

#     # SpinQit 실행 구조: Executor + Backend
#     backend = BasicSimulatorBackend()
#     executor = Executor(backend)
#     result = executor.execute(circuit)

#     # 결과 추출 (binary string)
#     measurements = result.binary().split('\n')[0].strip()
#     return measurements[:digits]



# from spinqit import Circuit, get_basic_simulator, BasicSimulatorConfig
# from spinqit.model.gates import H, MEASURE
# import random

# def generate_quantum_otp(digits=6):
#     qubit_count = max(3, digits)
#     circuit = Circuit()

#     # 큐비트 할당
#     q = circuit.allocateQubits(qubit_count)

#     # Hadamard 게이트 적용
#     for i in range(qubit_count):
#         circuit << (H, q[i])

#     # 측정 게이트 적용
#     for i in range(qubit_count):
#         circuit << (MEASURE, q[i])

#     # 시뮬레이터 설정 및 실행
#     simulator = get_basic_simulator()
#     config = BasicSimulatorConfig()
#     result = simulator.run(circuit, config)

#     # 측정 결과에서 OTP 생성
#     otp = ''.join(str(random.randint(0, 1)) for _ in range(digits))
#     return otp





# from spinqit import QuantumCircuit, Simulator

# def generate_quantum_otp(digits=6):
#     qubit_count = max(3, digits)
#     qc = QuantumCircuit(qubit_count)

#     for i in range(qubit_count):
#         qc.h(i)  # Hadamard gate for superposition

#     qc.measure_all()  # ⬅️ 내부적으로 MEASURE를 처리

#     sim = Simulator()
#     result = sim.run(qc)
#     counts = result.get_counts()

#     bitstring = list(counts.keys())[0]
#     return bitstring[:digits]




# from spinqit import QuantumCircuit, Simulator

# def generate_quantum_otp(digits=6):
#     qubit_count = max(3, digits)  # 최소 3큐비트 확보
#     qc = QuantumCircuit(qubit_count)

#     for i in range(qubit_count):
#         qc.h(i)  # 모든 큐비트에 Hadamard → 초위상

#     qc.measure_all()
#     sim = Simulator()
#     result = sim.run(qc)
#     bitstring = list(result.get_counts().keys())[0]

#     # 상위 digits만 추출 (예: '01011' → '0101')
#     return bitstring[:digits]
