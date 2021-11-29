import * as React from "react";
import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";
import Button from "@mui/material/Button";
import { CountryData } from "../data/CountryData";
import { CountryStateMap } from "../data/CountryStateMap";
import { TypeData } from "../data/TypeData";
import { DateData } from "../data/DateData";

// when user selects a country, the next input field will only show states from that country.
// use a dictonary for that
// https://javascript.plainenglish.io/how-to-use-the-autocomplete-component-in-material-ui-11a7132d2b71?gi=eb1a40c3a4fe
export function AutocompleteInputField(props) {

	const handleChange = (event, newInput, reason) => {
		if (reason === "clear") {
			props.setInput("");
		} else {
			props.setInput(newInput);
		}
	};

	return (
		<div>
			<Autocomplete
				disablePortal
				id={`${props.InputLabel}-combo-box`}
				onInputChange={handleChange}
				value={props.input}
				options={props.InputOptions}
				sx={{ width: 200 }}
				renderInput={(params) => (
					<TextField {...params} label={props.InputLabel} />
				)}
			/>
		</div>
	);
}

// pass these inputs values back up using callback? or lifting
// when submit is pressed pass up the values and make GET request for table?
// https://stackoverflow.com/questions/55726886/react-hook-send-data-from-child-to-parent-component
export function SearchInputFields({ parentCallback }) {
	const [countryInput, setCountryInput] = React.useState("");
	const [stateInput, setStateInput] = React.useState("");
	const [typeInput, setTypeInput] = React.useState("");
	const [dateInput, setDateInput] = React.useState("");

	const countryOptions = CountryData;
	const countryStateMapOptions = CountryStateMap;
	const typeOptions = TypeData;
	const dateOptions = DateData;

	// pass back up the input values, then use those input values to make api call
	const handleSubmit = (event) => {
		// console.log(countryInput);
		// console.log(stateInput);
		// console.log(typeInput);
		// console.log(dateInput);

		const inputValues = {
			countryVal: countryInput,
			stateVal: stateInput,
			typeVal: typeInput,
			dateVal: dateInput,
		};

		// pass input values back to parent component
		parentCallback(inputValues);

	};

	return (
		<div style={{ display: "flex", flexWrap: "wrap" }}>
			<AutocompleteInputField
				InputLabel="Country"
				InputOptions={countryOptions}
				input={countryInput}
				setInput={setCountryInput}
			/>
			<AutocompleteInputField
				InputLabel="State"
				InputOptions={countryStateMapOptions[countryInput]}
				input={stateInput}
				setInput={setStateInput}
			/>
			<AutocompleteInputField
				InputLabel="Type"
				InputOptions={typeOptions}
				input={typeInput}
				setInput={setTypeInput}
			/>
			<AutocompleteInputField
				InputLabel="Date"
				InputOptions={dateOptions}
				input={dateInput}
				setInput={setDateInput}
			/>
			<Button
				onClick={handleSubmit}
				variant="outlined"
				style={{
					marginLeft: "2rem",
					borderColor: "#FFFFFF",
					color: "#FFFFFF",
				}}
			>
				Submit
			</Button>
		</div>
	);
}