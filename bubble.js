function bubble_sort(arr){
    let is_swap = false
    let counter = 0
    for(let i=arr.length;i>=0;i--){
        let temp =0;
        
        for(let j=0;j<i-1;j++){
            if(arr[j]>arr[j+1]){
                is_swap = true
                temp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1] = temp
                
                
            }
        }
    }
    if(is_swap){
        counter = counter + 1
    }
    console.log(`Swap is :: ${counter}`)
    console.log(arr[0])
    console.log(arr[arr.length-1])
    
    return arr
}


arr = [1,5,2,7,6,0]
sorted_array = bubble_sort(arr)
console.log(sorted_array)