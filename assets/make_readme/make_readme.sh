#!/bin/bash
# This will be run inside nciccbr/make_readme:latest docker

MDPATH="assets/make_readme"
# MDPATH="/Users/kopardevn/Documents/GitRepos/.github/assets/make_readme"
# add banner
cat ${MDPATH}/banner.md > README_tmp.md

# add toc
echo -ne "<!-- TOC --> \n\n" >> README_tmp.md

# add latest releses
echo -ne "## NEW Releases \n\n" >> README_tmp.md
python ${MDPATH}/get_recent_releases_table.py --nmonths 3 >> README_tmp.md

# top contributors
echo -ne "## TOP contributors \n\n" >> README_tmp.md
python ${MDPATH}/get_per_user_commits.py >> README_tmp.md

# about us
cat ${MDPATH}/about_us.md >> README_tmp.md
cat ${MDPATH}/back_to_top.md >> README_tmp.md

# our model
cat ${MDPATH}/our_model.md >> README_tmp.md
cat ${MDPATH}/back_to_top.md >> README_tmp.md

# add pipelines
cat ${MDPATH}/pipelines.md >> README_tmp.md
cat ${MDPATH}/back_to_top.md >> README_tmp.md

# add tools
cat ${MDPATH}/tools.md >> README_tmp.md
cat ${MDPATH}/back_to_top.md >> README_tmp.md

# pipeliner release history
cat ${MDPATH}/ccbrpipeliner_release_history.md >> README_tmp.md
cat ${MDPATH}/back_to_top.md >> README_tmp.md

# add list of all releases releses
# echo -ne "## Latest Releases of pipelines/tools: \n\n" >> README_tmp.md
cat ${MDPATH}/latest_releases.md >> README_tmp.md
python ${MDPATH}/get_recent_releases_table.py >> README_tmp.md
cat ${MDPATH}/back_to_top.md >> README_tmp.md

# member activities
echo -ne "\n## Days since last activity \n\n -1=No activity found!\n\n" >> README_tmp.md
python ${MDPATH}/get_last_activity_per_member.py >> README_tmp.md
echo -ne "\n\n" >> README_tmp.md
cat ${MDPATH}/back_to_top.md >> README_tmp.md

# add citation
cat ${MDPATH}/citation.md >> README_tmp.md
cat ${MDPATH}/back_to_top.md >> README_tmp.md

# add toc
python ${MDPATH}/add_toc.py --input README_tmp.md --output profile/README.md

rm -f README_tmp.md