function criaLinha(cars) {
	linha = document.createElement("tr");

	make = document.createElement("td");
	model = document.createElement("td");
	cylinders = document.createElement("td");
	year = document.createElement("td");
	transmission = document.createElement("td");
	drive=document.createElement("td");
	fuel_type=document.createElement("td");
	
	make.innerHTML = cars.make;
	model.innerHTML = cars.model;
	cylinders.innerHTML = cars.cylinders;
	year.innerHTML = cars.year;
	transmission.innerHTML = cars.transmission;
	drive.innerHTML = cars.drive;
	fuel_type.innerHTML = cars.fuel_type;
		
	linha.appendChild(make);
	linha.appendChild(model);
	linha.appendChild(cylinders);
	linha.appendChild(year);
	linha.appendChild(transmission);
	linha.appendChild(drive);
	linha.appendChild(fuel_type);
	return linha;
}


function ApiCardData(modelo) {
	
	const options = {
		method: 'GET',
		url: 'https://api.api-ninjas.com/v1/cars?limit=30&model=' + modelo,
		headers: {
			'X-Api-Key': '<>'
		},
	};

	axios.request(options).then(function (response) {
		let cars = response.data;
		let tabela = document.getElementById("tabela")
		cars.forEach(element => {
			
			let linha = criaLinha(element);
			tabela.appendChild(linha);
		});
		
	}).catch(function (error) {
		console.error(error);
	});


}

const options = {
	method: 'GET',
	url: 'https://api.api-ninjas.com/v1/cars?limit=30&model=',
	headers: {
		'X-Api-Key': '<>'
	},
};

axios.request(options).then(function (response) {
	let cars = response.data;
	let tabela = document.getElementById("tabela")
	cars.forEach(element => {
		
		let linha = criaLinha(element);
		tabela.appendChild(linha);
	});
	
}).catch(function (error) {
	console.error(error);
});

