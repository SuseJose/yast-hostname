require "cfa/base_model"
require "cfa/augeas_parser"
require "cfa/matcher"

module Y2Caasp
  module CFA
    # Represents a Salt Minion master configuration file.
    class MinionMasterConf < ::CFA::BaseModel
      attributes(master: "master")

      # Configuration parser
      #
      # FIXME: At this time, we're using Augeas' cobblersettings lense because,
      # although the file is in yaml format, it doesn't have a YAML header
      # which is required by the yaml lense.
      PARSER = ::CFA::AugeasParser.new("cobblersettings.lns")
      # Path to configuration file
      PATH = "/etc/salt/minion.d/master.conf".freeze

      # Constructor
      #
      # @param file_handler [.read, .write, nil] an object able to read/write a string.
      def initialize(file_handler: nil)
        super(PARSER, PATH, file_handler: file_handler)
      end

      # FIXME: This class should we moved to be easy reused by other modules as for example
      # yast-configuration-management is also defining it
      def master=(master_name)
        # FIXME: the cobblersettings lense does not support dashes in the value
        # without single quotes, we need to use a custom lense for salt conf.
        # As Salt can use also 'master' just use in case of dashed.
        data["master"] = master_name.include?("-") ? "'#{master_name}'" : master_name
      end
    end
  end
end
