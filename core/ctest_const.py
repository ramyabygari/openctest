# constant for ctest generation

import os

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
APP_DIR = os.path.join(CUR_DIR, "app")
GEN_CTEST_DIR = os.path.join(CUR_DIR, "generate_ctest")
RUN_CTEST_DIR = os.path.join(CUR_DIR, "run_ctest")

HCOMMON = "hadoop-common"
HDFS = "hadoop-hdfs"
HBASE = "hbase-server"
ZOOKEEPER = "zookeeper-server"
ALLUXIO = "alluxio-core"
HIVE = "hive-common"
NIFI = "nifi-common"
FLINK = "flink-core"
CAMEL = "camel-core"
HYARNCOMMON = "hadoop-yarn-common"
KCOMMON = "kylin-common"


CTEST_HADOOP_DIR = os.path.join(APP_DIR, "ctest-hadoop")
CTEST_HBASE_DIR = os.path.join(APP_DIR, "ctest-hbase")
CTEST_ZK_DIR = os.path.join(APP_DIR, "ctest-zookeeper")
CTEST_ALLUXIO_DIR = os.path.join(APP_DIR, "ctest-alluxio")
CTEST_HIVE_DIR = os.path.join(APP_DIR, "ctest-hive")
CTEST_NIFI_DIR = os.path.join(APP_DIR, "ctest-nifi")
CTEST_FLINK_DIR = os.path.join(APP_DIR, "ctest-flink")
CTEST_CAMEL_DIR = os.path.join(APP_DIR, "ctest-camel")
CTEST_KYLIN_DIR = os.path.join(APP_DIR, "ctest-kylin")

PROJECT_DIR = {
    HCOMMON: CTEST_HADOOP_DIR,
    HDFS: CTEST_HADOOP_DIR,
    HBASE: CTEST_HBASE_DIR,
    ZOOKEEPER: CTEST_ZK_DIR,
    ALLUXIO: CTEST_ALLUXIO_DIR,
    HIVE: CTEST_HIVE_DIR,
    NIFI: CTEST_NIFI_DIR,
    FLINK: CTEST_FLINK_DIR,
    CAMEL: CTEST_CAMEL_DIR,
    HYARNCOMMON: CTEST_HADOOP_DIR,
    KCOMMON: CTEST_KYLIN_DIR,
}


# the module of the project we experimented on
MODULE_SUBDIR = {
    HCOMMON: "hadoop-common-project/hadoop-common",
    HDFS: "hadoop-hdfs-project/hadoop-hdfs",
    HBASE: "hbase-server",
    ZOOKEEPER: "zookeeper-server",
    ALLUXIO: "core",
    HIVE: "common",
    NIFI: "nifi-common",
    FLINK: "flink-core",
    CAMEL: "core/camel-core",
    HYARNCOMMON: "hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common",
    KCOMMON: "core-common",
}


# surefire report
SUREFIRE_SUBDIR = "../target/surefire-reports/"
SUREFIRE_XML = "TEST-{}.xml" # slot is the classname
HIVE_SUREFIRE_XML =  "TEST-org.apache.hadoop.hive.conf.{}.xml" # slot is the classname
SUREFIRE_XML_NIFI = "TEST-org.apache.nifi.util.{}.xml" # slot is the classname
SUREFIRE_TXT = "{}.txt" # testclass
SUREFIRE_OUTTXT = "{}-output.txt" #testclass 

SUREFIRE_DIR = {
    HCOMMON: [os.path.join(CTEST_HADOOP_DIR, MODULE_SUBDIR[HCOMMON], SUREFIRE_SUBDIR)],
    HDFS: [os.path.join(CTEST_HADOOP_DIR, MODULE_SUBDIR[HDFS], SUREFIRE_SUBDIR)],
    HBASE: [os.path.join(CTEST_HBASE_DIR, MODULE_SUBDIR[HBASE], SUREFIRE_SUBDIR)],
    ZOOKEEPER: [os.path.join(CTEST_ZK_DIR, MODULE_SUBDIR[ZOOKEEPER], SUREFIRE_SUBDIR)],
    ALLUXIO: [
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "base", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "client/fs", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "client/hdfs", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "common", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "server/common", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "server/proxy", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "server/worker", SUREFIRE_SUBDIR),
        os.path.join(CTEST_ALLUXIO_DIR, MODULE_SUBDIR[ALLUXIO], "server/master", SUREFIRE_SUBDIR),
    ],
    HIVE: [os.path.join(CTEST_HIVE_DIR, MODULE_SUBDIR[HIVE], SUREFIRE_SUBDIR)],
    NIFI: [os.path.join(CTEST_NIFI_DIR, MODULE_SUBDIR[NIFI],"nifi-properties", SUREFIRE_SUBDIR)],
    FLINK: [os.path.join(CTEST_FLINK_DIR, MODULE_SUBDIR[FLINK], SUREFIRE_SUBDIR)],
    CAMEL: [os.path.join(CTEST_HADOOP_DIR, MODULE_SUBDIR[CAMEL], SUREFIRE_SUBDIR)],
    HYARNCOMMON: [os.path.join(CTEST_HADOOP_DIR, MODULE_SUBDIR[HYARNCOMMON], SUREFIRE_SUBDIR)],
    KCOMMON: [os.path.join(CTEST_KYLIN_DIR, MODULE_SUBDIR[KCOMMON], SUREFIRE_SUBDIR)],
}

# default or deprecate conf path
DEPRECATE_CONF_DIR = os.path.join(CUR_DIR, "deprecated_configs")
DEFAULT_CONF_DIR = os.path.join(CUR_DIR, "default_configs")

DEPRECATE_CONF_FILE = {
    HCOMMON: os.path.join(DEPRECATE_CONF_DIR, "hadoop.list"),
    HDFS: os.path.join(DEPRECATE_CONF_DIR, "hadoop.list")
}

DEFAULT_CONF_FILE = {
    HCOMMON: os.path.join(DEFAULT_CONF_DIR, HCOMMON + "-default.tsv"),
    HDFS: os.path.join(DEFAULT_CONF_DIR, HDFS + "-default.tsv"),
    HBASE: os.path.join(DEFAULT_CONF_DIR, HBASE + "-default.tsv"),
    ALLUXIO: os.path.join(DEFAULT_CONF_DIR, ALLUXIO + "-default.tsv"),
    ZOOKEEPER: os.path.join(DEFAULT_CONF_DIR, ZOOKEEPER + "-default.tsv"),
    HIVE: os.path.join(DEFAULT_CONF_DIR, HIVE + "-default.tsv"),
    NIFI: os.path.join(DEFAULT_CONF_DIR, NIFI + "-default.tsv"),
    FLINK: os.path.join(DEFAULT_CONF_DIR, FLINK + "-default.tsv"),
    CAMEL: os.path.join(DEFAULT_CONF_DIR, CAMEL + "-default.tsv"),
    HYARNCOMMON: os.path.join(DEFAULT_CONF_DIR, HYARNCOMMON + "-default.tsv"),
    KCOMMON: os.path.join(DEFAULT_CONF_DIR, KCOMMON + "-default.tsv"),
}


# injecting config file location
INJECTION_PATH = {
    HCOMMON: [
        os.path.join(CTEST_HADOOP_DIR, "hadoop-common-project/hadoop-common/target/classes/core-ctest.xml")
    ],
    HDFS: [
        os.path.join(CTEST_HADOOP_DIR, "hadoop-hdfs-project/hadoop-hdfs/target/classes/core-ctest.xml"),
        os.path.join(CTEST_HADOOP_DIR, "hadoop-hdfs-project/hadoop-hdfs/target/classes/hdfs-ctest.xml")
    ],
    HBASE: [
        os.path.join(CTEST_HBASE_DIR, "hbase-server/target/classes/core-ctest.xml"),
        os.path.join(CTEST_HBASE_DIR, "hbase-server/target/classes/hbase-ctest.xml")
    ],
    ZOOKEEPER: [
        os.path.join(CTEST_ZK_DIR, "zookeeper-server/ctest.cfg")
    ],
    ALLUXIO: [
        os.path.join(CTEST_ALLUXIO_DIR, "core/alluxio-ctest.properties")
    ],
    HIVE: [
        os.path.join(CTEST_HIVE_DIR, "conf/hive-ctest.xml")
    ],
    NIFI: [
        os.path.join(CTEST_NIFI_DIR, "nifi-commons/nifi-properties/src/test/resources/NiFiProperties/conf/ctest.properties")
    ],
    FLINK: [
        os.path.join(CTEST_FLINK_DIR, "flink-core/core-ctest.yaml")
    ],
    CAMEL: [
        os.path.join(CTEST_CAMEL_DIR, "core/camel-core/camel-ctest.properties")
    ],
    HYARNCOMMON: [
        os.path.join(CTEST_HADOOP_DIR, "hadoop-yarn-project/hadoop-yarn/hadoop-yarn-common/target/classes/yarn-common-ctest.xml")
    ],
    KCOMMON: [
        os.path.join(CTEST_KYLIN_DIR, "core-common/src/main/resources/ctest.properties")
        # os.path.join(CTEST_KYLIN_DIR, "core-common/target/ctest.properties")
    ],
}


# constants for ctest generation -- generated test result file
GENCTEST_TR_DIR = os.path.join(GEN_CTEST_DIR, "test_result") # test result directory
os.makedirs(GENCTEST_TR_DIR, exist_ok=True)
TR_FILE = "test_result_{id}.tsv"
MT_FILE = "missing_test_{id}.list"
FAIL = "f" # test failed
PASS = "p" # test passed
GOOD_VAL = "GOOD"
BAD_VAL = "BAD"
SKIP_VAL = "SKIP"

CTESTS_DIR = os.path.join(GEN_CTEST_DIR, "ctest_mapping")
os.makedirs(CTESTS_DIR, exist_ok=True)
CTESTS_FILE = "ctests-{project}.json"

# constants for running ctests
RUNCTEST_TR_DIR = os.path.join(RUN_CTEST_DIR, "run_ctest_result") # test result directory
os.makedirs(RUNCTEST_TR_DIR, exist_ok=True)