rm ~/blacklist.zip
cd ~/.pyenv/versions/3.9.16/envs/bl/lib/python3.9/site-packages/
zip -r9 ~/blacklist.zip .
cd ~/blacklist/
zip -g ~/blacklist.zip -r . -x '*.git*'
aws lambda update-function-code --function-name Blacklist --zip-file fileb://~/blacklist.zip --publish