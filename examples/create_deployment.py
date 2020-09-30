from camunda.endpoints import deployment

diagram_content = b"""
    <?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" xmlns:di="http://www.omg.org/spec/DD/20100524/DI" id="Definitions_1knttt0" targetNamespace="http://bpmn.io/schema/bpmn" exporter="Camunda Modeler" exporterVersion="4.2.0">
  <bpmn:process id="Process_0pvsd1t" isExecutable="true">
    <bpmn:startEvent id="StartEvent_1">
      <bpmn:outgoing>Flow_1mqi06m</bpmn:outgoing>
    </bpmn:startEvent>
    <bpmn:endEvent id="Event_0klyfpb">
      <bpmn:incoming>Flow_1mqi06m</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:sequenceFlow id="Flow_1mqi06m" sourceRef="StartEvent_1" targetRef="Event_0klyfpb" />
  </bpmn:process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_1">
    <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Process_0pvsd1t">
      <bpmndi:BPMNEdge id="Flow_1mqi06m_di" bpmnElement="Flow_1mqi06m">
        <di:waypoint x="215" y="97" />
        <di:waypoint x="272" y="97" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNShape id="_BPMNShape_StartEvent_2" bpmnElement="StartEvent_1">
        <dc:Bounds x="179" y="79" width="36" height="36" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Event_0klyfpb_di" bpmnElement="Event_0klyfpb">
        <dc:Bounds x="272" y="79" width="36" height="36" />
      </bpmndi:BPMNShape>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</bpmn:definitions>
""".strip()

response = deployment.create(
    deployment.CreateDeploymentRequest(
        deployment_name="MyDeployment",
        enable_duplicate_filtering=False,
        deploy_changed_only=False,
        deployment_source="diagram.bpmn",
        tenant_id="tenant",
        data=("diagram.bpmn", diagram_content),
    )
)
print(response)
