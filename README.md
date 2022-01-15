# Technical Debts and Faults in Open-source Quantum Software Systems: An Empirical Study


### Abstract
Quantum computing is a rapidly growing field attracting the interest of both researchers and software developers. Supported by its numerous open-source tools, developers can now build, test, or run their quantum algorithms.  Although the maintenance practices for traditional software systems have been extensively studied, the maintenance of quantum software is still a new field of study but a critical part to ensure the quality of a whole quantum computing system. In this work, we set out to investigate the distribution and evolution of technical debts in quantum software and their relationship with fault occurrences. Understanding these problems could guide future quantum development and provide maintenance recommendations for the key areas where quantum software developers and researchers should pay more attention. In this paper, we empirically studied 118 open-source quantum projects, which were selected from GitHub. The projects are categorized into 10 categories. We found that the studied quantum software suffers from the issues of code convention violation, error-handling, and code design. We also observed a statistically significant correlation between code design, redundant code or code convention, and the occurrences of faults in quantum software.

#### Highlights
- The quantum software systems suffer from code convention violation, error-handling, and code redundancy, mostly in the initial versions.

- There is a statistically significant correlation between technical debts (such as code convention, error-handling, redundant code, cognitive complexity of code) and fault occurrences in quantum software systems.


- The quantum software developers should use the existing static analysis tools to examine their code. Code reviewers and quantum quality assurance team should pay attention to the code quality and code size, especially when new files are added. %Code reviewers and quantum quality assurance team should use metrics like code convention, code redundancy, error-handling, and the cognitive complexity of the code to predict faulty commits.

- New tools should be introduced to support identifying quantum-specific problems, such as the technical debts and faults that only occur in a quantum software system. %Future works are appealed to study other aspects of quantum software in terms of maintenance and reliability.

- Future works are appealed to study other aspects of quantum software in terms of maintenance and reliability, such as code review, verification methods to ensure the correctness of a quantum program, and practical fault detection techniques for supporting quantum systematic testing and debugging.



##### Table of Contents  
- [Studied-Quantum-projects](#Studied-Quantum-projects)  
List of the studied quantum projects

- [Source](#Source)  
Descriptions of the most important source codes contains in this repository

- [Datasets](#Datasets)  
This provides the descriptions of the datasets contains in this repository

- [Figures](#Figures)  
Details of the plots and figures embedded in this repository is described here   


## Studied-Quantum-projects

| Repository        | Snapshots           | Category  |
| ------------- |:-------------:| -----:|
| qrefine/qrefine     | right-aligned | Quantum Algorithsm |
| mabuchilab/QNET     | centered      |   Quantum Algorithsm |
| Qiskit/qiskit-aqua  | are neat      |    Quantum Algorithsm |



|Repository|Category|commits|Size|Releases|Stars|Snapshots|Created_at|Age|Language|Descriptions|
| ---------|:-------|:-----:|:---|:------:|:---:|:-------:|:--------:|:---:|:-----:|----------:|
|Qiskit/qiskit-terra|Full-stack Library|3452|51762|56|2782|15|2017-03-03T17:02:42Z|1302|Python|Terra provides the foundations for Qiskit. It allows the user to write quantum circuits easily, and takes care of the constraints of real hardware.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|microsoft/Quantum|Full-stack Library|228|37677|1963|2878|11|2017-11-08T23:24:33Z|1051|PowerShell|Microsoft Quantum Development Kit Samples|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|microsoft/QuantumLibraries|Full-stack Library|268|12831|1896|188|11|2018-10-23T18:26:23Z|701|C#|Q# libraries for the Quantum Development Kit|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|microsoft/Quantum-NC|Full-stack Library|101|1502|1882|79|8|2018-01-23T19:10:35Z|965|F#|Microsoft Quantum Computing Libraries for noncommercial use|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|rigetti/pyquil|Full-stack Library|957|69128|64|1033|15|2017-01-09T21:30:22Z|1354|Python|A Python library for quantum programming using Quil.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Qiskit/qiskit|Full-stack Library|612|96678|34|978|8|2018-12-12T22:04:07Z|652|Python|Qiskit is an open-source framework for working with noisy quantum computers at the level of pulses, circuits, and algorithms.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Qiskit/qiskit-ibmq-provider|Full-stack Library|365|1608|24|76|8|2018-12-26T15:22:11Z|637|Python|Qiskit Provider for accessing the quantum devices and simulators at IBMQ|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|qiskit-community/qiskit-js|Full-stack Library|367|4211|23|86|8|2017-11-21T09:34:29Z|1032|JavaScript|:atom_symbol: Qiskit (Quantum Information Science Kit) for JavaScript|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|qiskit-community/qiskit-vscode|Full-stack Library|321|7218|23|51|5|2018-07-19T15:59:16Z|704|HTML|Simplifying Qiskit to make developing quantum circuits and applications faster|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|rigetti/rpcq|Full-stack Library|114|342|23|53|7|2018-10-11T19:38:34Z|714|Common Lisp|The RPC framework and message specification for @rigetti Quantum Cloud Services.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|ProjectQ-Framework/ProjectQ|Full-stack Library|193|1005|16|625|11|2016-12-28T09:31:53Z|1367|Python|ProjectQ: An open source software framework for quantum computing|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|QuantumPackage/qp2|Full-stack Library|550|20402|16|22|6|2019-01-25T08:32:32Z|586|Fortran|Quantum Package : a programming environment for wave function methods|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|XanaduAI/strawberryfields|Full-stack Library|792|15802|15|377|10|2018-03-26T14:38:39Z|914|Python|Strawberry Fields is a full-stack Python library for designing, simulating, and optimizing continuous variable (CV) quantum optical circuits.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Blueqat/Blueqat|Full-stack Library|528|1043|10|245|8|2018-08-02T00:18:23Z|782|Python|Quantum Computer Library for Everyone|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|quantumlib/Cirq|Full-stack Library|1503|8593|9|2345|12|2017-12-14T23:41:49Z|1015|Python|A python framework for creating, editing, and invoking Noisy Intermediate Scale Quantum (NISQ) circuits.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|softwareQinc/staq|Full-stack Library|178|9634|3|44|5|2019-05-14T17:02:22Z|490|C++|A full-stack quantum processing toolkit|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|lanl/qmasm|Assembly|306|486|6|303|14|2016-07-08T20:10:22Z|1525|Python|Quantum macro assembler for D-Wave systems|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|XanaduAI/blackbird|Assembly|151|2959|3|28|6|2018-10-25T21:24:07Z|684|C++|Blackbird is a quantum assembly language for continuous-variable quantum computation, that can be used to program Xanadu's quantum photonics hardware and Strawberry Fields simulator.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|BBN-Q/pyqgl2|Assembly|130|1977|0|5|11|2017-04-10T18:44:19Z|1165|Python|An imperative Quantum Gate Language (QGL) embedded in python.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|artiste-qb-net/qubiter|Assembly|366|13129|0|95|11|2016-03-21T05:34:07Z|1655|HTML|Python tools for reading, writing, compiling, simulating quantum computer circuits. Includes numpy and tensorflow backends. ‚ÄúQuantum Space, the final frontier. These are the voyages of the starship Qubiter. Its five-year mission: to explore strange new worlds, to seek out new life and new civilizations, to boldly go where no man has gone before.‚Äù|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|BBN-Q/QGL.jl|Assembly|109|118|0|8|4|2016-12-20T14:47:00Z|1276|Julia|A performance orientated QGL compiler.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|theQRL/QRL|Cryptography|3556|14118|84|328|14|2016-10-16T14:32:40Z|1437|Python|Quantum Resistant Ledger |
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|exaexa/codecrypt|Cryptography|374|20181|19|244|19|2012-11-05T22:09:23Z|2851|C++|Post-quantum cryptography tool (THIS REPOSITORY IS ONLY A MIRROR OF THE MAIN ONE, PLEASE DO NOT FILE BUGS HERE)|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|mupq/pqm4|Cryptography|171|1677|1|77|9|2018-03-16T09:58:41Z|922|Assembly|Post-quantum crypto library for the ARM Cortex-M4|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|supernomad/quantum|Cryptography|416|752|28|44|6|2016-05-31T06:23:57Z|1504|Go|A lightweight, encrypted, WAN oriented, software defined network device.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|microsoft/qsharp-compiler|Compiler|201|4550|1881|335|6|2019-06-07T18:48:01Z|476|C#|Q# compiler, command line tool, and Q# language server|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|QE-Lab/OpenQL|Compiler|1101|11137|14|17|15|2017-04-13T14:16:16Z|1242|C++|Quantum compiler|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Quantomatic/pyzx|Compiler|282|26059|2|99|9|2018-07-02T10:37:07Z|809|OpenQASM|Python library for quantum circuit rewriting and optimisation using the ZX-calculus|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|arguelles/nuSQuIDS|Simulator|726|48312|1|10|21|2014-09-17T13:25:12Z|2196|C++|Neutrino oscillation software using SQuIDS.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|softwareQinc/qpp|Simulator|2619|284707|30|208|21|2014-03-21T20:00:40Z|2379|C++|A modern C++11 quantum computing library|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|QuantumBFS/YaoBlocks.jl|Simulator|307|516|27|14|6|2018-11-22T17:10:59Z|662|Julia|Standard basic quantum circuit simulator building blocks.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|issp-center-dev/HPhi|Simulator|1752|384920|22|42|19|2015-09-11T02:40:51Z|1839|Shell|Quantum Lattice Model Simulator Package|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|SoftwareQuTech/SimulaQron|Simulator|788|6661|21|68|11|2017-06-25T10:14:59Z|1175|Python|Quantum Network Simulator for Application Programming|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|QuantumBFS/Yao.jl|Simulator|477|14433|18|335|9|2018-04-13T13:47:02Z|895|Julia|Extensible, Efficient Quantum Algorithm Design for Humans.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Strilanc/Quirk|Simulator|1297|21709|16|497|16|2014-03-05T23:31:28Z|2395|JavaScript|A drag-and-drop quantum circuit simulator that runs in your browser. A toy for exploring and understanding small quantum circuits.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Qiskit/qiskit-aer|Simulator|495|13922|16|140|9|2018-12-17T19:58:16Z|647|Python|Aer is a high performance simulator for quantum circuits that includes noise models|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|qutip/qutip|Simulator|4105|20039|14|841|37|2012-10-09T06:20:46Z|2908|Python|QuTiP: Quantum Toolbox in Python|
|QuEST-Kit/QuEST|Simulator|1084|10500|14|150|13|2017-03-28T12:00:18Z|1273|C++|A multithreaded, distributed, GPU-accelerated simulator of quantum computers|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|vm6502q/qrack|Simulator|684|13360|12|54|11|2017-12-21T01:15:29Z|1008|C++|Comprehensive, GPU accelerated framework for developing universal virtual quantum processors|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|qulacs/qulacs|Simulator|503|1162|12|138|7|2018-10-05T05:39:51Z|704|C++|Variational Quantum Circuit Simulator for Quantum Computation Research|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|quantumlib/OpenFermion-Cirq|Simulator|230|1757|5|229|9|2018-03-20T00:58:53Z|920|Python|Quantum circuits for simulations of quantum chemistry and materials.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|microsoft/qmt|Simulator|841|67172|4|40|6|2018-02-23T21:14:58Z|845|Python|Qubit Modeling Tools (QMT) for computational modeling of quantum devices|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Approximates/dotBloch|Simulator|202|47053|4|0|6|2018-06-02T21:00:14Z|811|C#|quantum bit simulator build in Unity 3D engine.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Qiskit/qiskit-jku-provider|Simulator|215|283|2|12|4|2018-06-27T19:36:57Z|803|C++|A local provider which allows Qiskit to use a decision-diagrams quantum simulator from JKU|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|ngnrsaa/qflex|Simulator|1282|3509|1|54|6|2019-02-07T21:08:10Z|595|C++|Flexible Quantum Circuit Simulator (qFlex) implements an efficient tensor network, CPU-based simulator of large quantum circuits.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|aparent/QCViewer|Simulator|280|5013|6|17|9|2012-01-11T17:49:28Z|3141|C++|A visual quantum circuit design and simulation tool.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|rigetti/qvm|Simulator|414|1047|31|260|5|2018-11-20T22:14:22Z|674|Common Lisp|The @rigetti high-performance quantum virtual machine.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|marvel-nccr/quantum-mobile|Simulator|282|3286|27|44|10|2017-10-09T22:10:36Z|1076|Shell|A Virtual Machine for computational materials science|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|qrefine/qrefine|Quantum Algorithsm|807|176811|1|9|12|2017-04-04T04:32:01Z|1266|Python|Quantum Refinement Module|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|mabuchilab/QNET|Quantum Algorithsm|866|6996|33|42|22|2012-03-26T00:17:35Z|3098|Python|Computer algebra package for quantum mechanics and photonic quantum networks|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Qiskit/qiskit-aqua|Quantum Algorithsm|5424|49630|23|359|10|2018-06-12T20:46:28Z|836|Python|Quantum Algorithms & Applications in Python|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|quantumlib/OpenFermion|Quantum Algorithsm|392|3994|15|941|12|2017-09-21T22:10:28Z|1099|Python|The electronic structure package for quantum computers.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|rigetti/grove|Quantum Algorithsm|510|4579|12|301|8|2016-12-22T01:08:42Z|1373|Python|Quantum algorithms built using pyQuil.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|netket/netket|Quantum Algorithsm|1699|51340|12|198|9|2018-04-23T18:48:08Z|883|C++|Machine learning algorithms for many-body quantum systems |
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|XanaduAI/thewalrus|Quantum Algorithsm|739|14198|12|32|8|2018-05-11T18:49:44Z|856|Python|A library for the calculation of hafnians, Hermite polynomials and Gaussian boson sampling.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|qucontrol/krotov|Quantum Algorithsm|483|57175|10|25|7|2018-11-06T19:21:21Z|673|Python|Python implementation of Krotov's method for quantum optimal control|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|aeantipov/pomerol|Quantum Algorithsm|203|1925|7|20|25|2014-06-11T03:44:49Z|2278|C++|Exact diagonalization, Lehmann's representation, Two-particle Green's functions|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Q-solvers/EDLib|Quantum Algorithsm|354|605|7|17|9|2016-07-19T15:51:30Z|1415|C++|Exact diagonalization solver for quantum electron models|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|dwave-examples/factoring|Quantum Algorithsm|150|173|5|18|8|2018-03-20T16:56:03Z|912|Python|Factor numbers using a quantum computer|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|PanPalitta/phase_estimation|Quantum Algorithsm|229|1439|3|6|9|2014-11-27T00:07:35Z|1500|C++|This project apply reinforcement learning algorithms based on DE and PSO to optimize adaptive quantum-phase estimation.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|ProjectQ-Framework/FermiLib|Quantum Algorithsm|127|747|3|72|2|2017-05-01T05:46:51Z|1243|Python|FermiLib: Open source software for analyzing fermionic quantum simulation algorithms|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|JoshuaSBrown/QC_Tools|Quantum Algorithsm|271|13925|2|12|12|2016-03-30T04:22:06Z|1634|C++|This small repository provides functionality for calculating the charge transfer integrals between two molecules. |
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|BBN-Q/QGL|Experimentation|1144|3893|7|16|28|2016-01-21T20:58:01Z|1637|Python|Quantum Gate Language (QGL) is a domain specific language embedded in python for specifying quantum gate sequences.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|m-labs/artiq|Experimentation|7183|13214|31|223|26|2014-05-25T18:09:36Z|2314|Python|A leading-edge control system for quantum information experiments|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|sedabull/quantum-shell|Experimentation|150|2483|16|19|3|2015-01-27T06:51:10Z|1663|CoffeeScript|An experimental terminal emulator for the Atom text editor|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|iitis/QuantumInformation.jl|Experimentation|473|743|9|41|15|2014-09-11T12:15:35Z|2159|Julia|A Julia package for numerical computation in quantum information theory|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|qutech/qupulse|Experimentation|1878|8383|9|20|21|2015-01-27T13:27:55Z|2023|Python|Quantum Computing Toolkit for Qubit Control|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|lneuhaus/pyrpl|Experimentation|1529|185025|5|55|12|2016-05-14T14:09:14Z|1581|Python|pyrpl turns your RedPitaya into a powerful DSP device, especially suitable as a lockbox in quantum optics experiments.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|BBN-Q/Qlab|Experimentation|2289|13587|14|28|27|2012-01-27T15:20:23Z|3065|MATLAB|Measurement and control software for superconducting qubits.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|BBN-Q/PyQLab|Experimentation|1153|2372|4|15|20|2012-04-04T19:36:43Z|3024|Python|A python library for instrument control and superconducting QIP experiments. |
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|zlatko-minev/pyEPR|Experimentation|309|3631|2|23|9|2017-08-22T14:47:16Z|1128|Jupyter Notebook|Powerful, automated analysis and design of quantum microwave chips & devices [Energy-Participation Ratio and more]|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|evaleev/libint|ToolKit|1107|34752|44|104|54|2013-08-13T21:17:06Z|2597|C++|Libint: high-performance library for computing Gaussian integrals in quantum mechanics|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|qojulia/QuantumOptics.jl|ToolKit|434|5089|26|265|21|2016-03-16T22:05:35Z|1646|Julia|Library for the numerical simulation of closed as well as open quantum systems.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|jcmgray/quimb|ToolKit|1171|12146|14|121|19|2015-12-09T14:02:41Z|1749|Python|A python library for quantum information and many-body calculations including tensor networks.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|XanaduAI/pennylane|ToolKit|1398|27738|12|487|10|2018-04-17T16:45:42Z|892|Python|PennyLane is a cross-platform Python library for quantum machine learning, automatic differentiation, and optimization of hybrid quantum-classical computations|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|OriginQ/QPanda-2|ToolKit|450|15205|11|83|9|2018-06-05T08:23:20Z|840|C++|QPanda 2 is an open source quantum computing framework developed by  OriginQC that can be used to build, run, and optimize quantum algorithms. |
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|CQCL/pytket|ToolKit|192|15122|11|76|7|2018-07-11T09:39:17Z|805|nan|Python module for interfacing with the CQC t|ket> library of quantum software|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|bloomberg/quantum|ToolKit|237|2515|6|169|9|2018-07-11T20:40:04Z|806|C++|Powerful multi-threaded coroutine dispatcher and parallel execution engine|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|rigetti/forest-benchmarking|ToolKit|192|9883|6|29|5|2018-12-17T19:53:19Z|552|Python|A library for quantum characterization, verification, validation (QCVV), and benchmarking using pyQuil.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|QInfer/python-qinfer|ToolKit|1107|4249|4|69|20|2012-08-15T01:02:45Z|2909|Python|Library for Bayesian inference via sequential Monte Carlo for quantum parameter estimation.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|zoran-cuckovic/QGIS-visibility-analysis|ToolKit|128|4763|4|34|7|2014-02-08T08:00:12Z|2388|Python|Quantum GIS plugin for visibility analysis|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|qubekit/QUBEKit|ToolKit|361|2810|2|4|8|2019-04-10T09:17:09Z|534|Python|  Quantum Mechanical Bespoke Force Field Derivation Toolkit|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|tensorflow/quantum|ToolKit|198|15395|2|877|3|2020-02-06T19:58:35Z|231|Python|Hybrid Quantum-Classical Machine Learning in TensorFlow|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|redhat-cip/openstack-quantum-puppet|ToolKit|175|408|1|1|3|2012-09-29T22:01:47Z|585|Puppet|Deploy Quantum with Puppet|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|boschmitt/tweedledum|ToolKit|266|9261|1|41|1|2018-07-13T20:03:36Z|803|C++|C++17 Library for writing, manipulating, and optimizing quantum circuits|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|TRIQS/triqs|ToolKit|2259|14086|17|89|28|2013-07-17T16:06:50Z|2607|C++|a Toolbox for Research on Interacting Quantum Systems|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|QuTech-Delft/qtt|ToolKit|1342|60850|5|21|16|2016-04-19T16:06:57Z|1619|Python|Quantum Technology Toolbox https://qtt.readthedocs.io/|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|lmacken/quantumrandom|ToolKit|116|324|4|104|5|2012-04-15T05:18:10Z|3075|Python|Tools for utilizing the ANU Quantum Random Number Generator|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|qucat/qucat|ToolKit|637|16417|4|28|6|2018-11-08T12:39:33Z|670|HTML|Quantum Circuit Analyzer Tool|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Qiskit/qiskit-ignis|ToolKit|446|9093|4|90|9|2018-12-11T01:53:00Z|653|Python|Ignis provides tools for quantum hardware verification, noise characterization, and error correction.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|orbkit/orbkit|ToolKit|348|10846|2|55|20|2015-11-10T08:48:43Z|1773|Python|A Toolbox for Post-Processing Quantum Chemical Wavefunction Data|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|deepchem/deepchem|ToolKit|4319|449487|13|2145|20|2015-09-24T23:20:28Z|1828|Python|Democratizing Deep-Learning for Drug Discovery, Quantum Chemistry, Materials Science and Biology|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|aiidateam/aiida-quantumespresso|ToolKit|536|4400|13|21|13|2017-06-20T12:54:43Z|1189|Python|The official AiiDA plugin for Quantum ESPRESSO|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|shinmorino/sqaod|Quantum Annealing|991|66834|19|35|5|2017-10-24T13:39:16Z|903|C++|Solvers/annealers for simulated quantum annealing on CPU and CUDA(NVIDIA GPU).|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|dwavesystems/qbsolv|Quantum Annealing|394|41888|19|873|13|2017-01-06T18:18:22Z|1367|q|Qbsolv,a decomposing solver, finds a minimum value of a large quadratic unconstrained binary optimization (QUBO) problem by splitting it into pieces solved either via a D-Wave system or a classical tabu solver.   (Note that qbsolv by default uses its internal classical solver.  Access to a D-Wave system must be arranged separately.)|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|dwavesystems/dimod|Quantum Annealing|1540|2851|82|66|13|2017-08-18T01:02:17Z|1154|Python|A shared API for QUBO/Ising samplers.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|dwavesystems/dwave-system|Quantum Annealing|857|1662|48|53|15|2018-02-19T19:54:19Z|973|Python|An API for easily incorporating the D-Wave system as a sampler, either directly or through Leap's cloud-based hybrid samplers|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|dwavesystems/dwavebinarycsp|Quantum Annealing|269|413|14|11|9|2017-12-13T01:56:30Z|1001|Python|Map constraint satisfaction problems with binary variables to binary quadratic models.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|dwavesystems/penaltymodel|Quantum Annealing|570|572|60|12|11|2017-11-03T22:50:38Z|1076|Python|Utilities and interfaces for using penalty models.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|ValeevGroup/mpqc|Quantum-Chemistry|4481|364241|59|36|93|2013-08-15T15:28:10Z|2367|C++|The Massively Parallel Quantum Chemistry program, MPQC, computes properties of atoms and molecules from first principles using the time independent Schr√∂dinger equation.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|pyscf/pyscf|Quantum-Chemistry|7219|80151|56|381|26|2014-05-02T18:42:25Z|2338|Python|Python module for quantum chemistry|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|MolSSI-BSE/basis_set_exchange|Quantum-Chemistry|888|44582|41|61|12|2017-12-04T19:56:23Z|1009|Python|A repository for quantum chemistry basis sets|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|MolSSI/QCElemental|Quantum-Chemistry|790|1978|32|66|8|2018-08-31T17:37:37Z|739|Python|Periodic table, physical constants, and molecule parsing for quantum chemistry.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|MolSSI/QCEngine|Quantum-Chemistry|1067|1622|28|60|10|2018-03-01T22:25:35Z|923|Python|Quantum chemistry program executor and IO standardizer (QCSchema).|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|MolSSI/QCFractal|Quantum-Chemistry|2494|8274|26|85|14|2017-01-19T20:28:18Z|1336|Python|A distributed compute and database platform for quantum chemistry. |
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|SebWouters/CheMPS2|Quantum-Chemistry|652|180430|22|45|17|2013-11-18T15:29:44Z|2423|C++|CheMPS2: a spin-adapted implementation of DMRG for ab initio quantum chemistry|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|Quantum-Dynamics-Hub/libra-code|Quantum-Chemistry|690|365403|19|10|21|2017-08-24T09:07:06Z|1128|Jupyter Notebook|nan|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|QMCPACK/qmcpack|Quantum-Chemistry|9592|216665|14|124|39|2017-01-11T19:02:29Z|1352|C++|Main repository for QMCPACK, an open-source production level many-body ab initio Quantum Monte Carlo code for computing the electronic structure of atoms, molecules, and solids.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|cp2k/cp2k|Quantum-Chemistry|1215|190584|12|214|77|2018-10-02T10:42:51Z|724|Fortran|Quantum chemistry and solid state physics software package|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|votca/xtp|Quantum-Chemistry|3627|39463|11|20|47|2016-01-20T17:47:47Z|1709|C++|GW-BSE for excited state Quantum Chemistry in a Gaussian Orbital basis, electronic spectroscopy with QM/MM, charge and energy dynamics in complex molecular systems|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|hande-qmc/hande|Quantum-Chemistry|2998|99421|8|45|38|2015-04-21T09:45:14Z|1933|Fortran|Open source stochastic quantum chemistry|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|tmancal74/quantarhei|Quantum-Chemistry|987|5678|6|9|15|2016-07-20T18:30:25Z|1527|Python|Open Quantum System Theory for Molecular Systems|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|LCPQ/quantum_package|Quantum-Chemistry|2730|40575|5|30|20|2014-04-01T09:24:45Z|2368|Fortran|Set of quantum chemistry programs and libraries|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|vonDonnerstein/QuantumLab.jl|Quantum-Chemistry|186|58193|5|27|10|2015-10-02T10:35:39Z|1815|Julia|A workbench for Quantum Chemistry and Quantum Physics in Julia|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|ericchansen/q2mm|Quantum-Chemistry|629|7460|2|10|17|2014-08-26T00:21:27Z|2218|Python|Quantum to Molecular Mechanics (Q2MM)|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|aoterodelaroza/critic2|Quantum-Chemistry|1685|247637|2|41|19|2015-10-02T02:46:58Z|1819|Fortran|Analysis of quantum chemical interactions in molecules and solids.|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|GQCG/GQCP|Quantum-Chemistry|1500|70120|2|5|9|2018-08-23T12:10:29Z|763|C++|The Ghent Quantum Chemistry Package for electronic structure calculations|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|
|qcdb/qcdb|Quantum-Chemistry|360|5816|1|2|8|2018-02-15T20:52:04Z|917|Python|quantum chemistry common driver and databases|
| ---------|--------| -------|---| -------|-----| --------|----------| -----|------| ----------|




## Source



## Datasets


## Figures
