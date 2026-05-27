# [<img src="https://raw.githubusercontent.com/CCBR/.github/main/img/ccbrbanner.png">](https://bioinformatics.ccr.cancer.gov/ccbr/)

<!-- This file is generated from profile/README.qmd. Please edit that file, not the plain markdown file. -->

## Table of Contents

- [🎉 Recent Releases (last 3
  months)](#tada-recent-releases-last-3-months)
- [TOP contributors](#top-contributors)
- [About Us](#about-us)
  - [🆘 Need Help?](#sos-need-help)
- [Our model](#our-model)
- [Pipelines](#pipelines)
- [Tools](#tools)
- [`ccbrpipeliner` module release history on
  BIOWULF](#ccbrpipeliner-module-release-history-on-biowulf)
- [📦 Full Release History](#package-full-release-history)
- [Days since last activity](#days-since-last-activity)
- [Citation](#citation)

## 🎉 Recent Releases (last 3 months)

## TOP contributors

## About Us

- 👋 Hi, we’re the
  [**@CCBR**](https://bioinformatics.ccr.cancer.gov/ccbr/), a group of
  bioinformatics analysts and engineers
- 📖 We build flexible, reproducible, workflows for next-generation
  sequencing data
- 💡 We [collaborate](https://abcs-amp.nih.gov/project/request/CCBR/)
  with [CCR](https://ccr.cancer.gov/) PIs
- 📫 You can reach us at <ccbr_pipeliner@mail.nih.gov>
- 🏁 Check out our [release
  history](#ccbrpipeliner-module-release-history-on-biowulf)
- 🔗 Our [Zenodo](https://zenodo.org/communities/ccbr) community

### 🆘 Need Help?

📧 Email us at <ccbr_pipeliner@mail.nih.gov> — we’re always happy to
help!

🗓️ **Weekly Office Hours** — Thursdays, 3–5 PM - 📍 In-person: Bethesda
Campus, Building 37, Room 3041 - 💻 Virtual: [Join via Microsoft
Teams](https://teams.microsoft.com/meet/2207566172748?p=aoXDCUX4EFqcmCGmsK)

<hr>

<p align="center">

<a href="#table-of-contents">Back to Top</a>

</p>

## Our model

[<img src="https://raw.githubusercontent.com/CCBR/.github/main/img/CCBR_circle_diagram.png" width=600>](https://bioinformatics.ccr.cancer.gov/ccbr/)

Got data? We’ve got you covered! 🎉 The **CCR Collaborative
Bioinformatics Resource (CCBR)** is your one-stop shop for
bioinformatics support at the National Cancer Institute’s [Center for
Cancer Research (CCR)](https://ccr.cancer.gov/). We’re a powerhouse team
of bioinformatics experts drawn from across NCI — including the [CCR
Office of Science and Technology Resources
(OSTR)](https://ostr.ccr.cancer.gov/), the [Frederick National
Laboratory for Cancer Research (FNLCR)](https://frederick.cancer.gov/),
and the [Center for Biomedical Informatics and Information Technology
(CBIIT)](https://cbiit.cancer.gov/) — all united by one mission:
**turning your raw data into discovery**.

Whether you need help with experimental design, data analysis, pipeline
development, or training, we make it easy to get started. Just [submit a
request](https://bioinformatics.ccr.cancer.gov/ccbr/ask-for-help/) and
we’ll take it from there — with personalized consultations (in-person or
virtual!) tailored to your project’s needs. No bioinformatics background
required on your end; that’s literally what we’re here for. 🙌

We operate through two complementary teams that together keep CCR
researchers moving forward:

- 🏢 **The Core Team** — Our centralized squad available to any CCR
  researcher. From bulk RNA-seq to whole-genome analysis, we bring broad
  expertise and dedicated bandwidth to help you tackle the big
  questions.

- 🔬 **The Embedded Team** — Bioinformaticians embedded directly within
  specific labs and research groups, providing day-to-day, hands-on
  support with deep familiarity of your ongoing projects. Think of them
  as your in-house bioinformatics colleagues!

> 💡 Ready to get started? Visit [CCBR’s official
> website](https://bioinformatics.ccr.cancer.gov/ccbr/) or [reach out
> directly](https://bioinformatics.ccr.cancer.gov/ccbr/ask-for-help/) —
> we’d love to work with you!

<hr>

<p align="center">

<a href="#table-of-contents">Back to Top</a>

</p>

## Pipelines

CCBR offers end-to-end analysis pipelines for NGS data analysis.

Here is a list of our prominent pipelines and their release schedule on
BIOWULF:

| Data Type               | Pipeline Name                                                                                                                            | CLI<sup>\*</sup> available since |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| RNASeq<sup>1</sup>      | [RENEE](https://github.com/CCBR/RENEE)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg)       | July 3rd 2023                    |
| WESSeq<sup>2</sup>      | [XAVIER](https://github.com/CCBR/XAVIER)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg)     | July 21st 2023                   |
| ATACSeq<sup>3</sup>     | [ASPEN](https://github.com/CCBR/ASPEN)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg)       | November 30th 2023               |
| ChIPSeq<sup>4</sup>     | [CHAMPAGNE](https://github.com/CCBR/CHAMPAGNE)![nextflow](https://raw.githubusercontent.com/CCBR/.github/main/img/nextflow-small-v2.svg) | October 15th 2023                |
| CRISPRSeq<sup>5</sup>   | [CRISPIN](https://github.com/CCBR/CRISPIN)![nextflow](https://raw.githubusercontent.com/CCBR/.github/main/img/nextflow-small-v2.svg)     | September 2023                   |
| CUT&RunSeq<sup>6</sup>  | [CARLISLE](https://github.com/CCBR/CARLISLE)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg) | October 31st 2023                |
| EV-Seq<sup>10</sup>     | [ESCAPE](https://github.com/CCBR/ESCAPE)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg)     | March 26th 2024                  |
| circRNASeq<sup>7</sup>  | [CHARLIE](https://github.com/CCBR/CHARLIE)![snakemake](https://raw.githubusercontent.com/CCBR/.github/main/img/snakemake-small-v2.svg)   | September 16th 2024              |
| scRNASeq<sup>8</sup>    | [SINCLAIR](https://github.com/CCBR/SINCLAIR)![nextflow](https://raw.githubusercontent.com/CCBR/.github/main/img/nextflow-small-v2.svg)   | February 28th 2025               |
| WGSSeq<sup>9</sup>      | [LOGAN](https://github.com/CCBR/LOGAN)![nextflow](https://raw.githubusercontent.com/CCBR/.github/main/img/nextflow-small-v2.svg)         | May 31st 2025                    |
| spatialSeq<sup>11</sup> | [SPENCER](https://github.com/CCBR/SPENCER)![nextflow](https://raw.githubusercontent.com/CCBR/.github/main/img/nextflow-small-v2.svg)     | TBD                              |

<sup>\* CLI = Command Line Interface</sup>

> ℹ️ GUI (Graphical User Interface) development has been suspended for
> the time being but may resume in the future.

<sup> **1** RENEE=_Rna sEquencing aNalysis pipElinE_. Starts with raw
fastq files and ends with a counts matrix.</sup>

<sup> **2** XAVIER=_eXome Analysis and Variant explorER_.</sup>

<sup> **3** ASPEN=_Atac Seq PipEliNe_.</sup>

<sup> **4** CHAMPAGNE=_CHromAtin iMmuno PrecipitAtion sequencinG
aNalysis pipEline_.</sup>

<sup> **5** CRISPIN=_CRISPr screen sequencing analysis pipelINe_.
CRISPRSeq analysis with MAGeCK, drugZ and BAGEL2. </sup>

<sup> **6** CARLISLE=_Cut And Run anaLysIS pipeLinE_. Supports human and
mouse samples with (recommended) or without spike-ins.</sup>

<sup> **7** CHARLIE=_Circrnas in Host And viRuses anaLysis pIpEline_.
Finds known and novel circRNAs in human/mouse + virus genomes.</sup>

<sup> **8** SINCLAIR=_SINgle CelL AnalysIs Resource_.</sup>

<sup> **9** LOGAN=_whoLe genOme-sequencinG Analysis pipeliNe_.</sup>

<sup> **10** ESCAPE=_Extracellular veSiCles rnAseq PipelinE_.</sup>

<sup> **11** SPENCER=_SPatial sequENCing Resource_.</sup>

For any other datatype or pipeline, please [email us
📬](mailto:ccbr_pipeliner@mail.nih.gov) directly to get the conversation
started!

<hr>

<p align="center">

<a href="#table-of-contents">Back to Top</a>

</p>

## Tools

In addition to end-to-end analysis pipelines, the CCBR dev team also
builds tools for data management, metadata management, and HPC
utilities:

| Tool                                                 | Description                                                                                                                                                                |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [spacesavers2](https://github.com/CCBR/spacesavers2) | 🚀 Crawls HPC folders to identify duplicate files and report how much disk space can be reclaimed — essential for keeping Biowulf storage lean                             |
| [parkit](https://github.com/CCBR/parkit)             | 🅿️ Archives completed project data (folders or tarballs) from Biowulf/Helix to the [HPC-DME](https://hpcdmeweb.nci.nih.gov/login) CCBR_Archive vault for long-term storage |
| [permfix](https://github.com/CCBR/permfix)           | 🔐 Fixes folder and file permissions for Biowulf users — handy when shared project directories get locked down                                                             |

## `ccbrpipeliner` module release history on BIOWULF

`module load ccbrpipeliner` loads the default release of ccbrpipeliner
on BIOWULF. Each release comprises a unique combination of pipeline
versions bundled together.

> ⚠️ Older releases remain available on BIOWULF but may not function as
> originally intended — changes to HPC modules, dependencies, or system
> software over time can affect behavior. We recommend using the current
> default release whenever possible.

| Release        | Tool versions                                                                                                                                                                                                                                                                                                                                                                                                         | Released on         | Decommissioned on   |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------- |
| 1              | RENEE v2.1 <sup>@#</sup>                                                                                                                                                                                                                                                                                                                                                                                              | July, 10th 2023     | July, 14th 2023     |
| 2              | RENEE v2.2 <sup>@#</sup>                                                                                                                                                                                                                                                                                                                                                                                              | July, 14th 2023     | September, 5th 2023 |
| 3              | RENEE v2.2 <sup>@#</sup>,<br> XAVIER v2.0 <sup>@</sup>                                                                                                                                                                                                                                                                                                                                                                | July, 21st 2023     | \-                  |
| 4              | RENEE v2.5 <sup>@#</sup>,<br> XAVIER v3.0 <sup>@#</sup>                                                                                                                                                                                                                                                                                                                                                               | September, 5th 2023 | \-                  |
| 5              | RENEE v2.5 <sup>@#</sup>,<br> XAVIER v3.0 <sup>@#</sup>,<br> CARLISLE v2.4 <sup>@</sup>,<br> CHAMPAGNE v0.2 <sup>@</sup>,<br> CRUISE v0.1 <sup>@</sup>,<br> spacesavers2 v0.10 <sup>@</sup>,<br> permfix v0.6 <sup>@</sup>                                                                                                                                                                                            | October, 27th 2023  | \-                  |
| 6              | RENEE v2.5 <sup>@#</sup>,<br> XAVIER v3.0 <sup>@#</sup>,<br> CARLISLE v2.4 <sup>@</sup>,<br> CHAMPAGNE v0.3 <sup>@</sup>,<br> CRUISE v0.1 <sup>@</sup>,<br> ASPEN v1.0 <sup>@</sup>,<br> spacesavers2 v0.12 <sup>@</sup>,<br> permfix v0.6 <sup>@</sup>                                                                                                                                                               | February, 29th 2024 | \-                  |
| 7              | RENEE v2.6 <sup>@#</sup>,<br> XAVIER v3.1 <sup>@#</sup>,<br> CARLISLE v2.6 <sup>@</sup>,<br> CHAMPAGNE v0.4 <sup>@</sup>,<br> CHARLIE v0.11 <sup>@</sup>,<br> CRISPIN v1.0 <sup>@</sup> (previously CRUISE),<br> ASPEN v1.0 <sup>@</sup>,<br> spacesavers2 v0.14 <sup>@</sup>,<br> permfix v0.6 <sup>@</sup>,<br> ccbr_tools v0.1 <sup>@</sup>                                                                        | Jan, 10th 2025      | \-                  |
| 8<sup>\*</sup> | RENEE v2.7 <sup>@#</sup>,<br> XAVIER v3.2 <sup>@#</sup>,<br> CARLISLE v2.7 <sup>@</sup>,<br> CHAMPAGNE v0.5 <sup>@</sup>,<br> CHARLIE v0.12 <sup>@</sup>,<br> CRISPIN v1.2 <sup>@</sup>,<br> ASPEN v1.1 <sup>@</sup>,<br> ESCAPE v1.2 <sup>@</sup>,<br> LOGAN v0.3 <sup>@</sup>,<br> SINCLAIR v0.3 <sup>@</sup>,<br> spacesavers2 v0.14 <sup>@</sup>,<br> permfix v0.6 <sup>@</sup>,<br> ccbr_tools v0.4 <sup>@</sup> | Jul, 18th 2025      | \-                  |

> <sup>\*</sup> = Current DEFAULT version on BIOWULF
>
> <sup>@</sup> = CLI available
>
> <sup>\#</sup> = GUI available

> `module load ccbrpipeliner` is also available on HELIX. It only loads
> the **tools** and not the **pipelines** as HELIX does not have a job
> scheduler

<hr>

<p align="center">

<a href="#table-of-contents">Back to Top</a>

</p>

## 📦 Full Release History

<hr>

<p align="center">

<a href="#table-of-contents">Back to Top</a>

</p>

## Days since last activity

## Citation

Most of our end-to-end pipelines which have been used in published
research work have been made available to the entire bioinformatics
community via a Zenodo DOI. Please feel free to visit our [Zenodo
community page](https://zenodo.org/communities/ccbr). And if you use our
pipelines, don’t forget to cite us!
