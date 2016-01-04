############################################
#
# Possible values for conf/server role
# 
# Follows Splunk server.conf.spec closely
#
############################################

splunk_server_conf:
  general:
    pass4Symmkey: <password>
    * Encrypted password

    site: [dynamic|<site>]
    * The site where the system is located. Dynamic will use site attribute from inventory

    trustedIP: <IP address>
    * Trusted IP for SSO

  diskUsage:
    minFreeSpace: <num>
    * Specified in megabytes.
    * The default setting is 5000 (approx 5GB)

  sslConfig:
    sslKeysfilePassword: <password>
    * Encrypted password 

  license:
    master_uri: [dynamic|<uri>]
    * Dynamic will use inventory to detect

  clustering:
    mode: [master|slave|searchhead|disabled]
    * Defaults to disabled

    master_uri: [<uri> | clustermaster:stanzaName1, clustermaster:stanzaName2]
    * URI of the cluster master that this slave or searchhead should connect to.
    
    pass4SymmKey: <password>
    * Encrypted password
 
    multisite: [true|false]
    * Defaults to false

    replication_factor: <positive integer>
    * Defaults to 3

    site_replication_factor: <comma-separated string>
    * Defaults to origin:2,total:3
    * Note: no spaces allowed between comma separated values

    search_factor:  <positive integer>
    * Defaults to 2

    available_sites:
      - [site1]
      - [site2]
     * List of available sites
     * Defaults to an empty string. So if multisite is turned on this needs to be explicitly set

     cluster_label: [dynamic|<string>]
     * Defaults to an empty string.
     * Use dynamic to set automatically

  replication_port:
    port: <port>
    * Replication port

  replication_port_ssl:
    port: <port>

    rootCA: <filepath>
    * Certificate authority list
    * Autogenerated file under $SPLUNK_HOME/etc/auth/cacert.pem

    serverCert: <filepath>
    * Full path to the server certificate.
    * Autogenerated file under $SPLUNK_HOME/etc/auth/server.pem

    password: <string>
    * Encrypted password
  
  shclustering:
    mgmt_uri: [mgmt-URI | dynamic]
    * The management uri is used to identify the cluster member's own address to
      itself.
    * Use dynamic to set own adress automatically
   
    id: <GUID>
    * Unique identifier for this cluster as a whole, shared across all cluster
    members.
    * Create one, e.g. using python: $ python -c "import uuid; print str(uuid.uuid4()).upper()" 

    conf_deploy_fetch_url: [ <URL> | dynamic ]
    * Specifies the location of the deployer from which members fetch the
      configuration bundle.
    * This value must be set to a <URL> or dynamic in order for the configuration bundle to
      be fetched.
    * Set to dynamic to automatically set value
    * Defaults to empty.

    election: [True | False]
    * This is used to classify a cluster as static or dynamic (RAFT based). 
    * election = false means static captain, which is used for DR situation.
    * election = true means dynamic captain election enabled through RAFT protocol

    pass4SymmKey: <password>
    * Secret shared among the members in the search head cluster to prevent any
      arbitrary instance from connecting to the cluster.
    * All members must use the same value.
    * If set in the [shclustering] stanza, it takes precedence over any setting
      in the [general] stanza.

    replication_factor: <positive integer>
    * Determines how many copies of search artifacts are created in the cluster.
    * This must be set to the same value on all members.
    * Defaults to 3.

    shcluster_label = <string>
    * This specifies the label of the search head cluster
