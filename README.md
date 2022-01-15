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
- [Studied Quantum projects](#Studied Quantum projects)  
List of the studied quantum projects

- [Source](#Source)  
Descriptions of the most important source codes contains in this repository

- [Datasets](#Datasets)  
This provides the descriptions of the datasets contains in this repository

- [Figures](#Figures)  
Details of the plots and figures embedded in this repository is described here   


## Studied Quantum projects


## Source



## Datasets


## Figures
