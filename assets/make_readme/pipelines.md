
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
