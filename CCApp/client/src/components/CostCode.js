import React, {useState, useEffect} from "react";
import {Button, Card} from 'react-bootstrap'

function CostCode({code, name, uom, billCodes, id}) {

    function handleClick(e) {
        console.log(e.target)
        console.log(id)
        fetch(`/phase_codes/${id}/bill_codes`)
            .then((r)=>r.json())
            .then((data)=>console.log(data))
    }


    return (
        <Card>
            <Card.Title>${code} - ${name}</Card.Title>
            <Card.Body>
                <Button variant="secondary" onClick={handleClick} >Show Details</Button>
            </Card.Body>
        </Card>
    
    )
}

export default CostCode;