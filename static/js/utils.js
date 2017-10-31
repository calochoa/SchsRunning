function parseURL() {
        const params = {}; // Bonus points for using CONST
        const keyValues = location.search.substr(1).split('&');
        if (keyValues[0] === '') {
          return {};
        }
        for (let i=0; i<keyValues.length; i++) {
          const keyValue = keyValues[i].split('=');
          const key = keyValue[0];
          let value = keyValue[1]; // Bonus points for using LET
          params[key] = value;
        }

        return params;
      }