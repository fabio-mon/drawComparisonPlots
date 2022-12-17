
# drawComparisonPlots
Small python package to produce comparison plots from root TTree data with the standard CMS layout. The plotter can be configured via python configuration files in the style of CMSSW.       

## Usage example       
```
python drawComparisonPlots.py --settings settings_compare_rewLOfake_cHHH1  --outdir path/to/output/
```
Few comments about the configuration file:        
* It should be provided to drawComparisonPlots.py without `.py` at the end       
* It can import settings from other configuration files through the normal python syntax       
* Custom function on the TTree branches can be defined in a separate c++ macro, see for example DeltaRmin.C, and then loaded within the configuration file, with r.gROOT.ProcessLineSync(".x DeltaRmin.C+")       