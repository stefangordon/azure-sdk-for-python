# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Graph
  module Models
    #
    # Server response for Get tenant groups API call
    #
    class GroupListResult

      include MsRestAzure

      # @return [Array<ADGroup>] Gets or sets the list of groups.
      attr_accessor :value

      # @return [String] Gets or sets the URL to get the next set of results.
      attr_accessor :odatanext_link


      #
      # Mapper for GroupListResult class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'GroupListResult',
          type: {
            name: 'Composite',
            class_name: 'GroupListResult',
            model_properties: {
              value: {
                required: false,
                serialized_name: 'value',
                type: {
                  name: 'Sequence',
                  element: {
                      required: false,
                      serialized_name: 'ADGroupElementType',
                      type: {
                        name: 'Composite',
                        class_name: 'ADGroup'
                      }
                  }
                }
              },
              odatanext_link: {
                required: false,
                serialized_name: 'odata\\.nextLink',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end