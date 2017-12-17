  /*
         * param1 Array 
         * param2 Array
         * return true or false
         */
        function arraysSimilar(arr1, arr2) {
            if (arr1 instanceof Array && arr2 instanceof Array) {
                if (arr1 !== null && arr2 !== null) {
                    len1 = arr1.length;
                    len2 = arr2.length;
                    var result1 = [];
                    var result2 = [];
                    if (len1 === len2) {
                        for (var i = 0; i < len1; i++) {
                            //判断数据类型是否为null
                            if (arr1[i] === null) {
                                result1[i] = "null";
                            }
                            //判断数据类型是否为日期       
                            else if (arr1[i] instanceof Date) {
                                result1[i] = "date";
                            }
                            //判断是否为window
                            else if (arr1[i] === window) {
                                result1[i] = "window";
                            } else {
                                result1[i] = typeof (arr1[i]);
                            }
                        }


                        for (var i = 0; i < len1; i++) {
                            //判断数据类型是否为null
                            if (arr2[i] === null) {
                                result2[i] = "null";
                            }
                            //判断数据类型是否为日期       
                            else if (arr2[i] instanceof Date) {
                                result2[i] = "date";
                            }
                            //判断是否为window
                            else if (arr2[i] === window) {
                                result2[i] = "window";
                            } else {
                                result2[i] = typeof (arr2[i]);
                            }
                        }

                        result1.sort();
                        result2.sort();
                        return result1.toString() === result2.toString();
                    }
                }


            } else {
                return false;
            }

        }