# [CCR Collaborative Bioinformatics Resource](https://bioinformatics.ccr.cancer.gov/ccbr/)

### About Us
- 👋 Hi, we're the [**@CCBR**](https://bioinformatics.ccr.cancer.gov/ccbr/), a group of bioinformatics analysts and engineers
- 📖 We build flexible, reproducible, workflows for next-generation sequencing data
- :bulb: We [collaborate](https://abcs-amp.nih.gov/project/request/CCBR/) with CCR PIs
- 📫 You can reach us at [ccbr_pipeliner@mail.nih.gov](mailto:ccbr_pipeliner@mail.nih.gov)
- 🏁 Check out our [release history](#release-history)

> <b><ins>RHEL8 BIOWULF updates:</ins></b>
> 
> [Biowulf](https://hpc.nih.gov) recently migrated to [RHEL8](https://hpc.nih.gov/docs/rhel8.html). We are aware that our module `ccbrpipeliner` on Biowulf is not functioning after the RHEL8 migration. We are diligently working on bringing `ccbrpipeliner` suite of pipelines back on-line for our Biowulf users. At the same time, we are also taking this opportunity to modernize and containerize our end-to-end pipeline offerings. These changes will minimize, if not eliminate, the pipelines' dependencies on other Biowulf modules and make `ccbrpipeliner` "operating system and HPC" - agnostic.
> 
> Here is our tentative schedule for bringing our various pipelines back on BIOWULF:
> 
> | Data Type | Pipeline Name | CLI<sup>*</sup> availability date | GUI<sup>*</sup> availability date |
> | --- | --- | --- |--- |
> | RNASeq<sup>1</sup> | [RENEE](https://github.com/CCBR/RENEE) | July, 3rd 2023 | July, 14th 2023 |
> | WESSeq<sup>2</sup> | [XAVIER](https://github.com/CCBR/XAVIER) | July, 21th 2023 | Sep, 1st 2023 |
> | ATACSeq<sup>3</sup> | [ASPEN](https://github.com/CCBR/ASPEN) | Coming Soon | Coming Soon |
> | ChIPSeq<sup>4</sup> | [CHAMPAGNE](https://github.com/CCBR/CHAMPAGNE) | Coming Soon | Coming Soon |
> | CRISPRSeq<sup>5</sup> | [CRUISE](https://github.com/CCBR/CRUISE) | Coming Soon | Coming Soon |
> | CUT&RunSeq<sup>6</sup> | [CARLISLE](https://github.com/CCBR/CARLISLE) | TBD | TBD |
> | circRNASeq<sup>7</sup> | [CHARLIE](https://github.com/CCBR/CHARLIE) | TBD | TBD |
> | scRNASeq<sup>8</sup> | [SINCLAIR](https://github.com/CCBR/SINCLAIR) | TBD | TBD |
> | WGSSeq<sup>9</sup> | [LOGAN](https://github.com/CCBR/LOGAN) | TBD | TBD |
>
> <sup>* CLI = Command Line Interface </sup>
>
> <sup>* GUI = Graphical User Interface </sup>
> 
> <sup> **1** RENEE=_Rna sEquencing aNalysis pipElinE_ starts with raw fastq files and ends with counts matrix. Downstream DEG support will be added at a later date. In the mean time you can use NIDAP or [iDEP](http://bioinformatics.sdstate.edu/idep/0) for DEG analysis.</sup>
> 
> <sup> **2** XAVIER=_eXome Analysis and Variant explorER_ will be soon available on Biowulf.</sup>
> 
> <sup> **3** ASPEN=_Atac Seq PipEliNe_ has limited support for differential ATACSeq signal analysis. CCBR has other pipelines for footprinting analysis like TOBIAS. Please reach out for details.</sup>
> 
> <sup> **4** CHAMPAGNE=_CHromAtin iMmuno PrecipitAtion sequencinG aNalysis pipEline_. CCBR plans to completely revamp ChIPSeq and may not be available until Q4 of 2023. In the interim, we recommend using the [ENCODE pipeline](https://hpc.nih.gov/apps/chipseq_pipeline.html) on biowulf for ChIPSeq analsyis.</sup>
> 
> <sup> **5** CRUISE=_Crispr scReen seqUencIng analySis pipEline_. CRISPRSeq analysis with MAGeCK, drugZ and BAGEL2. </sup>
> 
> <sup> **6** CARLISLE=_Cut And Run anaLysIS pipeLinE_ supports human and mouse samples with (recommended) or without spike-ins.</sup>
> 
> <sup> **7** CHARLIE=_Circrnas in Host And viRuses anaLysis pIpEline_ finds known and novel circRNAs in human/mouse + virus genomes. Differential circRNA analysis is planned for future.</sup>
> 
> <sup> **8** SINCLAIR=_SINgle CelL AnalysIs Resource_ addresses various single cell modalities... eg. single-cell expression, CITESeq, TCR-Seq, etc.</sup>
> 
> <sup> **9** WGSSeq pipeline will soon be CCBR's newest offering.</sup>
> 
> For any other datatype or pipeline, please [email :mailbox:](mailto:ccbr_pipeliner@mail.nih.gov) us directly to get the conversation started! 

### Release History

`module load ccbrpipeliner` loads default release of ccbrpipeliner. The complete list can also be viewed [here](https://github.com/CCBR/guis/tags). Each release comprises of a unique combination of the version numbers of the different pipelines offered as part of the ccbrpipeliner suite.

| Release | Tool versions | Released on | Decommissioned on |
| --- | --- | --- | --- |
| 1 | RENEE v2.1 (CLI/GUI) | July, 10th 2023 | July, 14th 2023 |
| 2 | RENEE v2.2 (CLI/GUI) | July, 14th 2023 | September, 5th 2023 |
| 3 | RENEE v2.2 (CLI/GUI), XAVIER v2.0 (CLI only)| July, 21st 2023 | - |
| 4 | RENEE v2.5 (CLI/GUI), XAVIER v3.0 (CLI/GUI)| September, 5th 2023 | - |

<hr>
<p align="center">
	<a href="##ccr-collaborative-bioinformatics-resource">Back to Top</a>
</p>
