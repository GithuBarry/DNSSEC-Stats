# DNSSEC-Stats
Use [DNSVIZ](https://github.com/dnsviz/dnsviz) to measure DNSSEC deployment and produce statistics on generated warnings.

We use top `top-1m.csv` ranking from https://statvoo.com/dl/top-1million-sites.csv.zip. Data retrived on Dec. 20, 2020. From it, we generated `top10000.csv`.

We tested on `authoritative DNS servers` and recursive servers including `1.1.1.1`, `8.8.8.8`, `114.114.114.114`, and `223.5.5.5`. We ran all probes on a Linode in Fremont, CA, United States. The experiment was carried out  in Dec. 20, 2020 - Jan. 5, 2021.

## Outcomes JSONs

To see our final outcomes, go to any folder under `Linode Results` and find files named as `results_*.json`. These files include results of running DNSSEC analysis of `top10000.csv`  (but not including domains listed in `probe_actual_failures.txt` in the same folder). 

(e.g. See [warning stats for Cloudfare DNS](https://github.com/GithuBarry/DNSSEC-Stats/blob/main/Linode%20Results/Cloudfare1111/results_warning_stats.json) or [the complete results](https://github.com/GithuBarry/DNSSEC-Stats/blob/main/Linode%20Results/Cloudfare1111/results_warnings.json) on domains in our [top10000.csv](https://github.com/GithuBarry/DNSSEC-Stats/blob/main/Linode%20Results/Cloudfare1111/top10000.csv) except [these failures](https://github.com/GithuBarry/DNSSEC-Stats/blob/main/Linode%20Results/Cloudfare1111/probe_actual_failures.txt)).

Among the 10000 domains we probed, each recursive DNS server fails <20 domains, but in the authoritative case we failed to probe 482 domains.

## Workflow used

Our workflow includes 1) gathering probe data 2) generate reports on warnings 3) clean up 4) produce data. This procedure can be seen in any folder in`Linode Results`. 

In the authorative case, we further run delegation status analyzer and its clean up procedures.

## Raw probe data zips

In Linode, I copied the same python working directory multiple times when testing different data and I zip them as a back up of our probe data. These zip files are in `Linode Results Zips`. Most of the zip files contains only the probing data (so only 1st step) without later analysis and can be a bit messy. Note that `Linode Results` have renamed and new running scripts and thus more clear than those in the zips (e.g. clean up script was not included in zips).

