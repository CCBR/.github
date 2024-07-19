[<img src="https://raw.githubusercontent.com/CCBR/.github/main/img/ccbrbanner.png">](https://bioinformatics.ccr.cancer.gov/ccbr/)
## Table of Contents

  - [NEW Releases](#new-releases)
  - [TOP contributors](#top-contributors)
  - [About Us](#about-us)
  - [Our model](#our-model)
  - [Pipelines](#pipelines)
  - [Tools](#tools)
  - [Release History](#release-history)
  - [Latest Releases of pipelines/tools:](#latest-releases-of-pipelines/tools:)
  - [Citation](#citation) 

## NEW Releases

| Repo Name                                            | Release Name                                                               | Release Date   |   Open Issues |
|:-----------------------------------------------------|:---------------------------------------------------------------------------|:---------------|--------------:|
| [spacesavers2](https://github.com/CCBR/spacesavers2) | [v0.14.0](https://github.com/CCBR/spacesavers2/releases/tag/v0.14.0)       | 2024-07-16     |             5 |
| [XAVIER](https://github.com/CCBR/XAVIER)             | [v3.0.3](https://github.com/CCBR/XAVIER/releases/tag/v3.0.3)               | 2024-07-11     |             9 |
| [ESCAPE](https://github.com/CCBR/ESCAPE)             | [v1.1.2](https://github.com/CCBR/ESCAPE/releases/tag/v1.1.2)               | 2024-06-27     |             1 |
| [permfix](https://github.com/CCBR/permfix)           | [v0.6.4](https://github.com/CCBR/permfix/releases/tag/v0.6.4)              | 2024-05-07     |             0 |
| [journal-club](https://github.com/CCBR/journal-club) | [jchelper 0.1.0](https://github.com/CCBR/journal-club/releases/tag/v0.1.0) | 2024-05-07     |             2 |
| [reports](https://github.com/CCBR/reports)           | [ccbr.reports 0.2.0](https://github.com/CCBR/reports/releases/tag/v0.2.0)  | 2024-04-30     |            11 |

## TOP contributors 

| User           |   Total Commits |   Commits in Last Month |   Commits in Last 6 Months |
|:---------------|----------------:|------------------------:|---------------------------:|
| kopardev       |            4114 |                      31 |                        528 |
| kelly-sovacool |            3310 |                     122 |                       1051 |
| slsevilla      |            1700 |                       0 |                        119 |
| skchronicles   |            1074 |                       0 |                          0 |
| dnousome       |             647 |                      13 |                        137 |
| kcgfarb        |             478 |                      28 |                        169 |
| finneyr        |             342 |                       1 |                         20 |
| samarth8392    |             339 |                      20 |                         99 |
| jlac           |             307 |                       0 |                          0 |
| kvaldez        |             222 |                       0 |                          0 |

## About Us

- 👋 Hi, we're the [**@CCBR**](https://bioinformatics.ccr.cancer.gov/ccbr/), a group of bioinformatics analysts and engineers
- 📖 We build flexible, reproducible, workflows for next-generation sequencing data
- :bulb: We [collaborate](https://abcs-amp.nih.gov/project/request/CCBR/) with [CCR](https://ccr.cancer.gov/) PIs
- 📫 You can reach us at [ccbr_pipeliner@mail.nih.gov](mailto:ccbr_pipeliner@mail.nih.gov)
- 🏁 Check out our [release history](#release-history)
- :link: Our [Zenodo](https://zenodo.org/communities/ccbr) community
<hr>
<p align="center">
	<a href="##table-of-contents">Back to Top</a>
</p>

## Our model

[<img src="https://raw.githubusercontent.com/CCBR/.github/main/img/CCBR_circle_diagram.png" width=600>](https://bioinformatics.ccr.cancer.gov/ccbr/)

<hr>
<p align="center">
	<a href="##table-of-contents">Back to Top</a>
</p>

## Pipelines

CCBR offers end-to-end analysis pipelines for NGS data analysis.

> <b><ins>RHEL8 BIOWULF updates:</ins></b>
> 
> In late 2023, [BIOWULF](https://hpc.nih.gov) migrated to a new operating system, [RHEL8](https://hpc.nih.gov/docs/rhel8.html). This migration rendered the Legacy functionality of CCBRPipeliner un-usable. We have been (and will continue to) work dilegently  to bring `ccbrpipeliner` suite of pipelines back on-line for our Biowulf users. At the same time, we are also taking this opportunity to not only increase our repetoire of pipelines but also modernize and containerize our end-to-end analysis offerings. These changes will minimize, if not eliminate, the pipelines' dependencies on other Biowulf modules and make `ccbrpipeliner` "operating system and HPC" - agnostic, thereby making it shareable with collaborators, and runnable on other HPCs (like [FRCE](https://ncifrederick.cancer.gov/staff/frce/welcome)) and beyond.
> 
Here is a list of our prominent pipelines and their release schedule on BIOWULF:
 
| Data Type | Pipeline Name | CLI<sup>*</sup> availability date | GUI<sup>*</sup> availability date |
| --- | --- | --- |--- |
| RNASeq<sup>1</sup> | [RENEE](https://github.com/CCBR/RENEE)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg) | July 3rd 2023 | July 14th 2023 |
| WESSeq<sup>2</sup> | [XAVIER](https://github.com/CCBR/XAVIER)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg) | July 21th 2023 | Sep 1st 2023 |
| ATACSeq<sup>3</sup> | [ASPEN](https://github.com/CCBR/ASPEN)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg) | November 30th 2023 | TBD |
| ChIPSeq<sup>4</sup> | [CHAMPAGNE](https://github.com/CCBR/CHAMPAGNE)![nextflow](https://raw.githubusercontent.com/CCBR/.github/main/img/nextflow-small-v2.svg) | October 15th 2023 | TBD |
| CRISPRSeq<sup>5</sup> | [CRISPIN](https://github.com/CCBR/CRISPIN)![nextflow](https://raw.githubusercontent.com/CCBR/.github/main/img/nextflow-small-v2.svg) | September 31st 2023 | TBD |
| CUT&RunSeq<sup>6</sup> | [CARLISLE](https://github.com/CCBR/CARLISLE)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg) | October 31st 2023 | TBD |
| EV-Seq<sup>10</sup> | [ESCAPE](https://github.com/CCBR/ESCAPE)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg) | March 26th, 2024 | TBD |
| circRNASeq<sup>7</sup> | [CHARLIE](https://github.com/CCBR/CHARLIE)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg) | _Jul 31st 2024_ | TBD |
| scRNASeq<sup>8</sup> | [SINCLAIR](https://github.com/CCBR/SINCLAIR)![nextflow](https://raw.githubusercontent.com/CCBR/.github/main/img/nextflow-small-v2.svg) | _Sep 30th 2024_ | TBD |
| WGSSeq<sup>9</sup> | [LOGAN](https://github.com/CCBR/LOGAN)![nextflow](https://raw.githubusercontent.com/CCBR/.github/main/img/nextflow-small-v2.svg) | _Sep 30th 2024_ | TBD |
| spatialSeq<sup>11</sup> | [SPENCER](https://github.com/CCBR/SPENCER)![nextflow](https://raw.githubusercontent.com/CCBR/.github/main/img/nextflow-small-v2.svg) | TBD | TBD |

<sup>* CLI = Command Line Interface </sup>
<sup>* GUI = Graphical User Interface </sup>

<sup> **1** RENEE=_Rna sEquencing aNalysis pipElinE_ starts with raw fastq files and ends with counts matrix. Downstream DEG support will be added at a later date. In the mean time you can use NIDAP or [iDEP](http://bioinformatics.sdstate.edu/idep96/) for DEG analysis.</sup>

<sup> **2** XAVIER=_eXome Analysis and Variant explorER_ will be soon available on Biowulf.</sup>

<sup> **3** ASPEN=_Atac Seq PipEliNe_ has limited support for differential ATACSeq signal analysis. CCBR has other pipelines for footprinting analysis like TOBIAS. Please reach out for details.</sup>

<sup> **4** CHAMPAGNE=_CHromAtin iMmuno PrecipitAtion sequencinG aNalysis pipEline_. CCBR plans to completely revamp ChIPSeq and may not be available until Q4 of 2023. In the interim, we recommend using the [ENCODE pipeline](https://hpc.nih.gov/apps/chipseq_pipeline.html) on biowulf for ChIPSeq analsyis.</sup>

<sup> **5** CRUISE=_Crispr scReen seqUencIng analySis pipEline_. CRISPRSeq analysis with MAGeCK, drugZ and BAGEL2. </sup>

<sup> **6** CARLISLE=_Cut And Run anaLysIS pipeLinE_ supports human and mouse samples with (recommended) or without spike-ins.</sup>

<sup> **7** CHARLIE=_Circrnas in Host And viRuses anaLysis pIpEline_ finds known and novel circRNAs in human/mouse + virus genomes. Differential circRNA analysis is planned for future.</sup>

<sup> **8** SINCLAIR=_SINgle CelL AnalysIs Resource_ addresses various single cell modalities... eg. single-cell expression, CITESeq, TCR-Seq, etc.</sup>

<sup> **9** LOGAN=_whoLe genOme-sequencinG Analysis pipeliNe_ will soon be CCBR's newest offering.</sup>

<sup> **10** ESCAPE=_Extracellular veSiCles rnAseq PipelinE_.</sup>

<sup> **11** SPENCER=_SPatial seqeENCing Resource_.</sup>

For any other datatype or pipeline, please [email :mailbox:](mailto:ccbr_pipeliner@mail.nih.gov) us directly to get the conversation started! 

<hr>
<p align="center">
	<a href="##table-of-contents">Back to Top</a>
</p>

## Tools

In additions to end-to-end analysis pipelines, the CCBR dev team also builds tools for data management, meta-data management, APIs, user management, etc. Here are some examples:

- [spacesavers2](https://github.com/CCBR/spacesavers2)
- [permfix](https://github.com/CCBR/permfix/)
- [pyrkit](https://github.com/CCBR/pyrkit)

<hr>
<p align="center">
	<a href="##table-of-contents">Back to Top</a>
</p>

## Release History

`module load ccbrpipeliner` loads default release of ccbrpipeliner. Each release comprises of a unique combination of the version numbers of the different pipelines offered as part of the ccbrpipeliner suite.

| Release | Tool versions | Released on | Decommissioned on |
| --- | --- | --- | --- |
| 1 | RENEE v2.1 <sup>@#</sup> | July, 10th 2023 | July, 14th 2023 |
| 2 | RENEE v2.2 <sup>@#</sup> | July, 14th 2023 | September, 5th 2023 |
| 3 | RENEE v2.2 <sup>@#</sup>, XAVIER v2.0 <sup>@</sup>| July, 21st 2023 | - |
| 4 | RENEE v2.5 <sup>@#</sup>, XAVIER v3.0 <sup>@#</sup>| September, 5th 2023 | - |
| 5 | RENEE v2.5 <sup>@#</sup>, XAVIER v3.0 <sup>@#</sup>, CARLISLE v2.4 <sup>@</sup>, CHAMPAGNE v0.2 <sup>@</sup>, CRUISE v0.1 <sup>@</sup>, spacesavers2 v0.10 <sup>@</sup>, permfix v0.6 <sup>@</sup> | October, 27th 2023 | - |
| 6<sup>*</sup> | RENEE v2.5 <sup>@#</sup>, XAVIER v3.0 <sup>@#</sup>, CARLISLE v2.4 <sup>@</sup>, CHAMPAGNE v0.3 <sup>@</sup>, CRUISE v0.1 <sup>@</sup>, ASPEN v1.0 <sup>@</sup>, spacesavers2 v0.12 <sup>@</sup>, permfix v0.6 <sup>@</sup> | February, 29th 2024 | - |

>
> <sup>*</sup> = Current DEFAULT version on BIOWULF
>
> <sup>@</sup> = CLI available
>  
> <sup>#</sup> = GUI available
<hr>
<p align="center">
	<a href="##table-of-contents">Back to Top</a>
</p>
## Latest Releases of pipelines/tools: 

| Repo Name                                                                                                                | Release Name                                                                                                    | Release Date   |   Open Issues |
|:-------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|:---------------|--------------:|
| [spacesavers2](https://github.com/CCBR/spacesavers2)                                                                     | [v0.14.0](https://github.com/CCBR/spacesavers2/releases/tag/v0.14.0)                                            | 2024-07-16     |             5 |
| [XAVIER](https://github.com/CCBR/XAVIER)                                                                                 | [v3.0.3](https://github.com/CCBR/XAVIER/releases/tag/v3.0.3)                                                    | 2024-07-11     |             9 |
| [ESCAPE](https://github.com/CCBR/ESCAPE)                                                                                 | [v1.1.2](https://github.com/CCBR/ESCAPE/releases/tag/v1.1.2)                                                    | 2024-06-27     |             1 |
| [permfix](https://github.com/CCBR/permfix)                                                                               | [v0.6.4](https://github.com/CCBR/permfix/releases/tag/v0.6.4)                                                   | 2024-05-07     |             0 |
| [journal-club](https://github.com/CCBR/journal-club)                                                                     | [jchelper 0.1.0](https://github.com/CCBR/journal-club/releases/tag/v0.1.0)                                      | 2024-05-07     |             2 |
| [reports](https://github.com/CCBR/reports)                                                                               | [ccbr.reports 0.2.0](https://github.com/CCBR/reports/releases/tag/v0.2.0)                                       | 2024-04-30     |            11 |
| [parkit](https://github.com/CCBR/parkit)                                                                                 | [v2.0.1](https://github.com/CCBR/parkit/releases/tag/v2.0.1)                                                    | 2024-04-16     |             0 |
| [CCBR_tobias](https://github.com/CCBR/CCBR_tobias)                                                                       | [CCBR_tobias 0.3.0](https://github.com/CCBR/CCBR_tobias/releases/tag/v0.3.0)                                    | 2024-04-12     |             1 |
| [RENEE](https://github.com/CCBR/RENEE)                                                                                   | [RENEE 2.5.12](https://github.com/CCBR/RENEE/releases/tag/v2.5.12)                                              | 2024-04-12     |            22 |
| [METRO](https://github.com/CCBR/METRO)                                                                                   | [v2.1](https://github.com/CCBR/METRO/releases/tag/v2.1)                                                         | 2024-03-28     |             2 |
| [CCBR-1144](https://github.com/CCBR/CCBR-1144)                                                                           | [Data Release Latest](https://github.com/CCBR/CCBR-1144/releases/tag/v1.0.0)                                    | 2024-03-04     |             0 |
| [CARLISLE](https://github.com/CCBR/CARLISLE)                                                                             | [v2.5.0](https://github.com/CCBR/CARLISLE/releases/tag/v.2.5.0)                                                 | 2024-02-26     |            13 |
| [TRANQUIL](https://github.com/CCBR/TRANQUIL)                                                                             | [TRANQUIL 0.2.1](https://github.com/CCBR/TRANQUIL/releases/tag/v0.2.1)                                          | 2024-02-22     |             0 |
| [ccbr1271_ERVpipeline](https://github.com/CCBR/ccbr1271_ERVpipeline)                                                     | [v1.0.3](https://github.com/CCBR/ccbr1271_ERVpipeline/releases/tag/v1.0.3)                                      | 2024-02-21     |             1 |
| [nf-sandbox](https://github.com/CCBR/nf-sandbox)                                                                         | [nf-sandbox 0.2.1](https://github.com/CCBR/nf-sandbox/releases/tag/v0.2.1)                                      | 2024-01-26     |             3 |
| [CHAMPAGNE](https://github.com/CCBR/CHAMPAGNE)                                                                           | [CHAMPAGNE 0.3.0](https://github.com/CCBR/CHAMPAGNE/releases/tag/v0.3.0)                                        | 2024-01-18     |            30 |
| [ASPEN](https://github.com/CCBR/ASPEN)                                                                                   | [v1.0.1](https://github.com/CCBR/ASPEN/releases/tag/v1.0.1)                                                     | 2023-12-27     |             6 |
| [CHARLIE](https://github.com/CCBR/CHARLIE)                                                                               | [v0.10.1](https://github.com/CCBR/CHARLIE/releases/tag/v0.10.1)                                                 | 2023-12-23     |            20 |
| [nf-modules](https://github.com/CCBR/nf-modules)                                                                         | [nf-modules 0.1.0](https://github.com/CCBR/nf-modules/releases/tag/v0.1.0)                                      | 2023-11-29     |            11 |
| [CRISPIN](https://github.com/CCBR/CRISPIN)                                                                               | [CRUISE 0.1.1](https://github.com/CCBR/CRISPIN/releases/tag/v0.1.1)                                             | 2023-11-06     |            14 |
| [SINCLAIR](https://github.com/CCBR/SINCLAIR)                                                                             | [v0.2.0](https://github.com/CCBR/SINCLAIR/releases/tag/v0.2.0)                                                  | 2023-11-01     |            26 |
| [CRISPRAnnotation](https://github.com/CCBR/CRISPRAnnotation)                                                             | [Code/Data Release](https://github.com/CCBR/CRISPRAnnotation/releases/tag/v1.0)                                 | 2023-10-19     |             0 |
| [SharanLab](https://github.com/CCBR/SharanLab)                                                                           | [Data/Code Release](https://github.com/CCBR/SharanLab/releases/tag/v1.0.0)                                      | 2023-07-18     |             0 |
| [Pipeliner](https://github.com/CCBR/Pipeliner)                                                                           | [v4.0.7](https://github.com/CCBR/Pipeliner/releases/tag/v4.0.7)                                                 | 2023-05-09     |            24 |
| [MAPLE](https://github.com/CCBR/MAPLE)                                                                                   | [version 1.0.1](https://github.com/CCBR/MAPLE/releases/tag/v1.0.1)                                              | 2023-02-27     |             0 |
| [DTB_ExomeSeq](https://github.com/CCBR/DTB_ExomeSeq)                                                                     | [v1.0](https://github.com/CCBR/DTB_ExomeSeq/releases/tag/v1.0)                                                  | 2022-06-22     |             0 |
| [ASCENT](https://github.com/CCBR/ASCENT)                                                                                 | [v0.1.1](https://github.com/CCBR/ASCENT/releases/tag/v0.1.1)                                                    | 2022-01-04     |             2 |
| [Antitumor-activity-of-entinostat-plus-NHS-IL12](https://github.com/CCBR/Antitumor-activity-of-entinostat-plus-NHS-IL12) | [Manuscript Methods](https://github.com/CCBR/Antitumor-activity-of-entinostat-plus-NHS-IL12/releases/tag/v.1.0) | 2021-06-01     |             0 |
| [CCBR_circRNA_AmpliconSeq](https://github.com/CCBR/CCBR_circRNA_AmpliconSeq)                                             | [v0.1.1](https://github.com/CCBR/CCBR_circRNA_AmpliconSeq/releases/tag/v0.1.1)                                  | 2021-03-24     |             0 |
| [rNA](https://github.com/CCBR/rNA)                                                                                       | [Release v1.0.0](https://github.com/CCBR/rNA/releases/tag/v1.0.0)                                               | 2021-01-21     |             0 |
| [l2p](https://github.com/CCBR/l2p)                                                                                       | [Release v0.0.3](https://github.com/CCBR/l2p/releases/tag/v0.0.3)                                               | 2020-07-13     |             0 |
| [MAAPster](https://github.com/CCBR/MAAPster)                                                                             | [Release v2.0.0](https://github.com/CCBR/MAAPster/releases/tag/v2.0.0)                                          | 2020-04-27     |             0 |
| [ChIP-Seq-Pipeline](https://github.com/CCBR/ChIP-Seq-Pipeline)                                                           | [Alpha 2](https://github.com/CCBR/ChIP-Seq-Pipeline/releases/tag/alpha2)                                        | 2016-10-01     |             2 |

<hr>
<p align="center">
	<a href="##table-of-contents">Back to Top</a>
</p>

## Citation

Most of our end-to-end pipelines which have been used in published research work have been made available to the entire bioinformatics community via a Zenodo DOI. Please feel free to visit our [Zenodo community page](https://zenodo.org/communities/ccbr). And if you use our pipelines, don't forget to cite us!
<hr>
<p align="center">
	<a href="##table-of-contents">Back to Top</a>
</p>
