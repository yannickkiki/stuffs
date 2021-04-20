#!/bin/bash

echo "removeing evaluation key"
rm  -rf ~/.IntelliJIdea*/config/eval
rm  -rf ~/.GoLand*/config/eval
rm  -rf ~/.WebStorm*/config/eval

rm -rf ~/.java/.userPrefs/jetbrains/goland
rm -rf ~/.java/.userPrefs/jetbrains/idea
rm -rf ~/.java/.userPrefs/jetbrains/webstorm

echo "resetting evalsprt in options.xml"
sed -i '/evlsprt/d' ~/.IntelliJIdea*/config/options/options.xml
sed -i '/evlsprt/d' ~/.IntelliJIdea*/config/options/other.xml

sed -i '/evlsprt/d' ~/.GoLand*/config/options/options.xml
sed -i '/evlsprt/d' ~/.GoLand*/config/options/other.xml
sed -i '/evlsprt/d' ~/.WebStorm*/config/options/options.xml
sed -i '/evlsprt/d' ~/.WebStorm*/config/options/other.xml

echo "resetting evalsprt in prefs.xml"
sed -i '/evlsprt/d' ~/.java/.userPrefs/prefs.xml


echo "change date file"
find ~/.IntelliJIdea* -type d -exec touch -t $(date +"%Y%m%d%H%M") {} +;
find ~/.IntelliJIdea* -type f -exec touch -t $(date +"%Y%m%d%H%M") {} +;

find ~/.GoLand* -type d -exec touch -t $(date +"%Y%m%d%H%M") {} +;
find ~/.GoLand* -type f -exec touch -t $(date +"%Y%m%d%H%M") {} +;

find ~/.WebStorm* -type d -exec touch -t $(date +"%Y%m%d%H%M") {} +;
find ~/.WebStorm* -type f -exec touch -t $(date +"%Y%m%d%H%M") {} +;
