echo $1

### Remove Python Compiled Files
shopt -s globstar
rm $SPLUNK_HOME/etc/apps/$1/bin/**/*.pyc
rm $SPLUNK_HOME/etc/apps/$1/bin/**/*.so
rm -r $SPLUNK_HOME/etc/apps/$1/bin/__pycache__
rm $SPLUNK_HOME/etc/apps/$1/lib/**/*.pyc
rm $SPLUNK_HOME/etc/apps/$1/lib/**/*.so
rm -r $SPLUNK_HOME/etc/apps/$1/lib/__pycache__

### Remove READMEs and metadata
rm -f $SPLUNK_HOME/etc/apps/$1/metadata/local.meta
rm -f $SPLUNK_HOME/etc/apps/$1/bin/README
rm -f $SPLUNK_HOME/etc/apps/$1/default/data/ui/views/README

### Remove the backup lookup file dir created by the lookup editor
rm -f $SPLUNK_HOME/etc/apps/$1/lookups/lookup_file_backups/

### Ensure permissions are correct
chmod -R u=rwX,g=r,o=r  $SPLUNK_HOME/etc/apps/$1/*
chmod -R -x+X $SPLUNK_HOME/etc/apps/$1/*
chmod -R u=rwx,g=r,o=r $SPLUNK_HOME/etc/apps/$1/bin/*

### Package App
rm $SPLUNK_HOME/etc/build/$1.spl
tar -cpzf $SPLUNK_HOME/etc/build/$1.spl -C $SPLUNK_HOME/etc/apps --exclude=$1/.* --exclude=$1/local $1 