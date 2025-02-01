import xml.etree.ElementTree as ET
import uuid

def create_pnml():
    pnml = ET.Element("pnml")
    net = ET.SubElement(pnml, "net", {
        "id": "net1",
        "type": "http://www.pnml.org/version-2009/grammar/pnml"
    })
    return pnml, net

def add_place(net, label):
    place_id = label
    place = ET.SubElement(net, "place", {"id": place_id})
    name = ET.SubElement(place, "name")
    text = ET.SubElement(name, "text")
    text.text = label

def add_transition(net, label):
    trans_id = label
    transition = ET.SubElement(net, "transition", {"id": trans_id})
    name = ET.SubElement(transition, "name")
    text = ET.SubElement(name, "text")
    text.text = label

def add_arc(net, source, target):
    arc_id = f"{source}_to_{target}"
    arc = ET.SubElement(net, "arc", {
        "id": arc_id,
        "source": source,
        "target": target
    })

def save_pnml(pnml, filename):
    tree = ET.ElementTree(pnml)
    with open(filename, "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)

def main():
    print("Creating PNML file...")
    
    print("Creating PNML structure...")
    
    pnml, net = create_pnml()
    
    p = add_place
    t = add_transition
    a = add_arc
    
    p(net, "business trip required")
    t(net, "file travel request")
    a(net, "business trip required", "file travel request")
    p(net, "travel request filed")
    a(net, "file travel request", "travel request filed")
    t(net, "check if travel request needs preliminary price inquiry")
    a(net, "travel request filed", "check if travel request needs preliminary price inquiry")
    p(net, "check if travel request needs preliminary price inquiry XOR")
    a(net, "check if travel request needs preliminary price inquiry", "check if travel request needs preliminary price inquiry XOR")
    t(net, "check if travel request needs preliminary price inquiry TRUE")
    a(net, "check if travel request needs preliminary price inquiry XOR", "check if travel request needs preliminary price inquiry TRUE")
    t(net, "check if travel request needs preliminary price inquiry FALSE")
    a(net, "check if travel request needs preliminary price inquiry XOR", "check if travel request needs preliminary price inquiry FALSE")
    p(net, "travel request needs no price inquiry")
    a(net, "check if travel request needs preliminary price inquiry FALSE", "travel request needs no price inquiry")
    t(net, "decide on approval requirements FROM travel request needs no price inquiry")
    a(net, "travel request needs no price inquiry", "decide on approval requirements FROM travel request needs no price inquiry")
    p(net, "decide on approval requirements XOR JOIN")
    a(net, "decide on approval requirements FROM travel request needs no price inquiry", "decide on approval requirements XOR JOIN")
    t(net, "decide on approval requirements")
    p(net, "travel request need price inquiry")
    a(net, "check if travel request needs preliminary price inquiry TRUE", "travel request need price inquiry")
    t(net, "prepare booking proposal FROM travel request need price inquiry")
    a(net, "travel request need price inquiry", "prepare booking proposal FROM travel request need price inquiry")
    p(net, "prepare booking proposal XOR JOIN")
    a(net, "prepare booking proposal FROM travel request need price inquiry", "prepare booking proposal XOR JOIN")
    t(net, "prepare booking proposal")
    a(net, "prepare booking proposal XOR JOIN", "prepare booking proposal")
    p(net, "booking proposal prepared")
    a(net, "prepare booking proposal", "booking proposal prepared")
    t(net, "send booking proposal to employee")
    a(net, "booking proposal prepared", "send booking proposal to employee")
    p(net, "booking proposal send")
    a(net, "send booking proposal to employee", "booking proposal send")
    t(net, "check booking proposal")
    a(net, "booking proposal send", "check booking proposal")
    p(net, "check booking proposal XOR")
    a(net, "check booking proposal", "check booking proposal XOR")
    t(net, "check booking proposal TRUE")
    a(net, "check booking proposal XOR", "check booking proposal TRUE")
    t(net, "check booking proposal FALSE")
    a(net, "check booking proposal XOR", "check booking proposal FALSE")
    p(net, "booking proposal not accepted")
    a(net, "check booking proposal FALSE", "booking proposal not accepted")	
    t(net, "check if price inquiry is still needed and up to date")
    a(net, "booking proposal not accepted", "check if price inquiry is still needed and up to date")
    p(net, "check if price inquiry is still needed and up to date XOR")
    a(net, "check if price inquiry is still needed and up to date", "check if price inquiry is still needed and up to date XOR")
    t(net, "check if price inquiry is still needed and up to date TRUE")
    a(net, "check if price inquiry is still needed and up to date XOR", "check if price inquiry is still needed and up to date TRUE")
    t(net, "check if price inquiry is still needed and up to date FALSE")
    a(net, "check if price inquiry is still needed and up to date XOR", "check if price inquiry is still needed and up to date FALSE")
    p(net, "price inquiry is no longer relevant")
    a(net, "check if price inquiry is still needed and up to date FALSE", "price inquiry is no longer relevant")
    p(net, "Price inquiry is still needed and up to date")
    a(net, "check if price inquiry is still needed and up to date TRUE", "Price inquiry is still needed and up to date")
    t(net, "request update of the booking proposal")
    a(net, "Price inquiry is still needed and up to date", "request update of the booking proposal")
    p(net, "update of booking proposal is requested")
    a(net, "request update of the booking proposal", "update of booking proposal is requested")
    a(net, "update of booking proposal is requested", "prepare booking proposal FROM update of booking proposal is requested")
    t(net, "prepare booking proposal FROM update of booking proposal is requested")
    a(net, "prepare booking proposal FROM update of booking proposal is requested", "prepare booking proposal XOR JOIN")
    p(net, "booking proposal is accepted")
    a(net, "check booking proposal TRUE", "booking proposal is accepted")
    t(net, "transform price inquiry to travel request")
    a(net, "booking proposal is accepted", "transform price inquiry to travel request")
    p(net, "price inquiry is transformed into travel request")
    a(net, "transform price inquiry to travel request", "price inquiry is transformed into travel request")
    t(net, "decide on approval requirements FROM price inquiry is transformed into travel request")
    a(net, "price inquiry is transformed into travel request", "decide on approval requirements FROM price inquiry is transformed into travel request")
    a(net, "decide on approval requirements FROM price inquiry is transformed into travel request", "decide on approval requirements XOR JOIN")
    a(net, "decide on approval requirements XOR JOIN", "decide on approval requirements")
    p(net, "decide on approval requirements XOR")
    a(net, "decide on approval requirements", "decide on approval requirements XOR")
    t(net, "decide on approval requirements TRUE")
    a(net, "decide on approval requirements XOR", "decide on approval requirements TRUE")
    t(net, "decide on approval requirements FALSE")
    a(net, "decide on approval requirements XOR", "decide on approval requirements FALSE")
    p(net, "travel needs to be approved >=500€")
    a(net, "decide on approval requirements FALSE", "travel needs to be approved >=500€")
    t(net, "forward request to approver FROM travel needs to be approved >=500€")
    a(net, "travel needs to be approved >=500€", "forward request to approver FROM travel needs to be approved >=500€")
    p(net, "forward request to approver XOR JOIN")
    a(net, "forward request to approver FROM travel needs to be approved >=500€", "forward request to approver XOR JOIN")
    t(net, "forward request to approver")
    a(net, "forward request to approver XOR JOIN", "forward request to approver")
    p(net, "request forwarded")
    a(net, "forward request to approver", "request forwarded")
    t(net, "decide on request")
    a(net, "request forwarded", "decide on request")
    p(net, "decide on request XOR")
    a(net, "decide on request", "decide on request XOR")
    t(net, "decide on request TRUE")
    a(net, "decide on request XOR", "decide on request TRUE")
    t(net, "decide on request FALSE")
    a(net, "decide on request XOR", "decide on request FALSE")
    t(net, "decide on request CORRECTION")
    a(net, "decide on request XOR", "decide on request CORRECTION")
    p(net, "request rejected")
    a(net, "decide on request FALSE", "request rejected")
    p(net, "request approved")
    a(net, "decide on request TRUE", "request approved")
    p(net, "travel does not need to be approved <500€")
    a(net, "decide on approval requirements TRUE", "travel does not need to be approved <500€")
    t(net, "check if booking is necessary FROM travel does not need to be approved <500€")
    a(net, "travel does not need to be approved <500€", "check if booking is necessary FROM travel does not need to be approved <500€")
    t(net, "check if booking is necessary FROM request approved")
    a(net, "request approved", "check if booking is necessary FROM request approved")
    p(net, "check if booking is necessary XOR JOIN")
    a(net, "check if booking is necessary FROM travel does not need to be approved <500€", "check if booking is necessary XOR JOIN")
    a(net, "check if booking is necessary FROM request approved", "check if booking is necessary XOR JOIN")
    p(net, "request needs to be corrected")
    a(net, "decide on request CORRECTION", "request needs to be corrected")
    t(net, "send request for correction")
    a(net, "request needs to be corrected", "send request for correction")
    p(net, "request for correction sent")
    a(net, "send request for correction", "request for correction sent")
    t(net, "correct request")
    a(net, "request for correction sent", "correct request")
    p(net, "request corrected")
    a(net, "correct request", "request corrected")
    t(net, "forward request to approver FROM request corrected")
    a(net, "request corrected", "forward request to approver FROM request corrected")
    a(net, "forward request to approver FROM request corrected", "forward request to approver XOR JOIN")
    t(net, "check if booking is necessary")
    a(net, "check if booking is necessary XOR JOIN", "check if booking is necessary")
    p(net, "check if booking is necessary XOR")
    a(net, "check if booking is necessary", "check if booking is necessary XOR")
    t(net, "check if booking is necessary TRUE")
    a(net, "check if booking is necessary XOR", "check if booking is necessary TRUE")
    t(net, "check if booking is necessary FALSE")
    a(net, "check if booking is necessary XOR", "check if booking is necessary FALSE")
    p(net, "booking is needed")
    a(net, "check if booking is necessary TRUE", "booking is needed")
    t(net, "prepare booking proposal FROM booking is needed")
    a(net, "booking is needed", "prepare booking proposal FROM booking is needed")
    p(net, "prepare booking proposal XOR JOIN")
    a(net, "prepare booking proposal FROM booking is needed", "prepare booking proposal XOR JOIN")
    t(net, "prepare booking proposal")
    a(net, "prepare booking proposal XOR JOIN", "prepare booking proposal")
    p(net, "booking proposal prepared")
    a(net, "prepare booking proposal", "booking proposal prepared")
    t(net, "send booking proposal to employee")
    a(net, "booking proposal prepared", "send booking proposal to employee")
    p(net, "booking proposal send")
    a(net, "send booking proposal to employee", "booking proposal send")
    t(net, "check booking proposal")
    a(net, "booking proposal send", "check booking proposal")
    p(net, "check booking proposal XOR")
    a(net, "check booking proposal", "check booking proposal XOR")
    t(net, "check booking proposal TRUE")
    a(net, "check booking proposal XOR", "check booking proposal TRUE")
    t(net, "check booking proposal FALSE")
    a(net, "check booking proposal XOR", "check booking proposal FALSE")
    p(net, "booking proposal not accepted")
    a(net, "check booking proposal FALSE", "booking proposal not accepted")
    t(net, "check if travel request is still needed and up to date")
    a(net, "booking proposal not accepted", "check if travel request is still needed and up to date")
    p(net, "check if travel request is still needed and up to date XOR")
    a(net, "check if travel request is still needed and up to date", "check if travel request is still needed and up to date XOR")
    t(net, "check if travel request is still needed and up to date TRUE")
    a(net, "check if travel request is still needed and up to date XOR", "check if travel request is still needed and up to date TRUE")
    t(net, "check if travel request is still needed and up to date FALSE")
    a(net, "check if travel request is still needed and up to date XOR", "check if travel request is still needed and up to date FALSE")
    p(net, "travel request is no longer relevant")
    a(net, "check if travel request is still needed and up to date FALSE", "travel request is no longer relevant")
    p(net, "travel request is still needed and up to date")
    a(net, "check if travel request is still needed and up to date TRUE", "travel request is still needed and up to date")
    t(net, "request update of the booking proposal")
    a(net, "travel request is still needed and up to date", "request update of the booking proposal")
    p(net, "update of booking proposal is requested")
    a(net, "request update of the booking proposal", "update of booking proposal is requested")
    t(net, "prepare booking proposal FROM update of booking proposal is requested")
    a(net, "update of booking proposal is requested", "prepare booking proposal FROM update of booking proposal is requested")
    a(net, "prepare booking proposal FROM update of booking proposal is requested", "prepare booking proposal XOR JOIN")
    p(net, "booking proposal accepted")
    a(net, "check booking proposal TRUE", "booking proposal accepted")
    t(net, "book travel")
    a(net, "booking proposal accepted", "book travel")
    p(net, "travel booked")
    a(net, "book travel", "travel booked")
    p(net, "booking is not needed")
    a(net, "check if booking is necessary FALSE", "booking is not needed")
    t(net, "Reporting FROM travel booked")
    a(net, "travel booked", "Reporting FROM travel booked")
    t(net, "Reporting FROM booking is not needed")
    a(net, "booking is not needed", "Reporting FROM booking is not needed")
    p(net, "Reporting XOR JOIN")
    a(net, "Reporting FROM travel booked", "Reporting XOR JOIN")
    a(net, "Reporting FROM booking is not needed", "Reporting XOR JOIN")
    t(net, "Reporting")
    a(net, "Reporting XOR JOIN", "Reporting")
    
    # Here we would split for reporting
    p(net, "travel completed")
    a(net, "Reporting", "travel completed")
    t(net, "check if expense documents exist")
    a(net, "travel completed", "check if expense documents exist")
    p(net, "check if expense documents exist XOR")
    a(net, "check if expense documents exist", "check if expense documents exist XOR")
    t(net, "check if expense documents exist TRUE")
    a(net, "check if expense documents exist XOR", "check if expense documents exist TRUE")
    t(net, "check if expense documents exist FALSE")
    a(net, "check if expense documents exist XOR", "check if expense documents exist FALSE")
    p(net, "no documents exist")
    a(net, "check if expense documents exist FALSE", "no documents exist")
    p(net, "documents exist")
    a(net, "check if expense documents exist TRUE", "documents exist")
    t(net, "upload travel expense documents")
    a(net, "documents exist", "upload travel expense documents")
    p(net, "expense documents uploaded")
    a(net, "upload travel expense documents", "expense documents uploaded")
    t(net, "file travel expense report FROM expense documents uploaded")
    a(net, "expense documents uploaded", "file travel expense report FROM expense documents uploaded")
    t(net, "file travel expense report FROM no documents exist")
    a(net, "no documents exist", "file travel expense report FROM no documents exist")
    p(net, "file travel expense report XOR JOIN")
    a(net, "file travel expense report FROM expense documents uploaded", "file travel expense report XOR JOIN")
    a(net, "file travel expense report FROM no documents exist", "file travel expense report XOR JOIN")
    t(net, "file travel expense report")
    a(net, "file travel expense report XOR JOIN", "file travel expense report")
    p(net, "travel expense report filed")
    a(net, "file travel expense report", "travel expense report filed")
    t(net, "confirm travel expense report")
    a(net, "travel expense report filed", "confirm travel expense report")
    p(net, "travel expense report confirmed")
    a(net, "confirm travel expense report", "travel expense report confirmed")
    t(net, "decide on travel expense approval FROM travel expense report confirmed")
    a(net, "travel expense report confirmed", "decide on travel expense approval FROM travel expense report confirmed")
    p(net, "decide on travel expense approval XOR JOIN")
    a(net, "decide on travel expense approval FROM travel expense report confirmed", "decide on travel expense approval XOR JOIN")
    t(net, "decide on travel expense approval")
    a(net, "decide on travel expense approval XOR JOIN", "decide on travel expense approval")
    p(net, "decide on travel expense approval XOR")
    a(net, "decide on travel expense approval", "decide on travel expense approval XOR")
    t(net, "decide on travel expense approval TRUE")
    a(net, "decide on travel expense approval XOR", "decide on travel expense approval TRUE")
    t(net, "decide on travel expense approval FALSE")
    a(net, "decide on travel expense approval XOR", "decide on travel expense approval FALSE")
    p(net, "expense report needs correction")
    a(net, "decide on travel expense approval FALSE", "expense report needs correction")
    t(net, "send request for travel expense correction")
    a(net, "expense report needs correction", "send request for travel expense correction")
    p(net, "request for travel expense correction sent")
    a(net, "send request for travel expense correction", "request for travel expense correction sent")
    t(net, "correct travel expense report")
    a(net, "request for travel expense correction sent", "correct travel expense report")
    p(net, "travel expense report is corrected")
    a(net, "correct travel expense report", "travel expense report is corrected")
    t(net, "decide on travel expense approval FROM travel expense report is corrected")
    a(net, "travel expense report is corrected", "decide on travel expense approval FROM travel expense report is corrected")
    a(net, "decide on travel expense approval FROM travel expense report is corrected", "decide on travel expense approval XOR JOIN")
    p(net, "expense report approved")
    a(net, "decide on travel expense approval TRUE", "expense report approved")
    t(net, "expense report approved AND")
    a(net, "expense report approved", "expense report approved AND")
    p(net, "expense report approved AND CALC")
    a(net, "expense report approved AND", "expense report approved AND CALC")
    t(net, "calculate payments")
    a(net, "expense report approved AND CALC", "calculate payments")
    p(net, "payments calculated")
    a(net, "calculate payments", "payments calculated")
    t(net, "pay expenses FROM payments calculated")
    a(net, "payments calculated", "pay expenses FROM payments calculated")
    p(net, "expense report approved AND SEND")
    a(net, "expense report approved AND", "expense report approved AND SEND")
    t(net, "send original documents to archive")
    a(net, "expense report approved AND SEND", "send original documents to archive")
    p(net, "documents archived")
    a(net, "send original documents to archive", "documents archived")
    t(net, "pay expenses FROM documents archived")
    a(net, "documents archived", "pay expenses FROM documents archived")
    p(net, "pay expenses AND JOIN")
    a(net, "pay expenses FROM payments calculated", "pay expenses AND JOIN")
    a(net, "pay expenses FROM documents archived", "pay expenses AND JOIN")
    t(net, "pay expenses")
    a(net, "pay expenses AND JOIN", "pay expenses")
    p(net, "expenses paid")
    a(net, "pay expenses", "expenses paid")
    
    
    print("Structure created.")
    
    save_pnml(pnml, "output.pnml")
    print("PNML file saved as 'output.pnml'")

if __name__ == "__main__":
    main()
