import React, {useEffect, useState} from "react";
import CostCode from "./CostCode";

function CostCodeList() {
    const [phaseCodes,setPhaseCodes] = useState([])
  
    useEffect(()=> {
      fetch('/phase_codes')
        .then((r)=>r.json())
        .then((codes)=>setPhaseCodes(codes))
    },[])

    const phaseElements = phaseCodes.map((code)=>{
        return <CostCode key={code.id} id={code.id} code={code.code} name={code.name} uom={code.uom} billCodes={code["bill_codes"]} />
    })

    console.log(phaseCodes)
    return (
        <div>
            {phaseElements} ? {phaseElements} : <h1>loading</h1>
        </div>
    )
}

export default CostCodeList