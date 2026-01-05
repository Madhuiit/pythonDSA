 function rotate(arr) {


    if(arr.length === 0){
        return arr
    }

    let  last = arr.length
    let rest = arr.slice(0,arr.length-1)
    

    return [last ,...rest]
}

console.log(rotate([1,2,3,4,5]))