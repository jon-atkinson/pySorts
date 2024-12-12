import React from "react";
import {
  Box,
  Button,
  MenuItem,
  Select,
  TextField,
  Checkbox,
  FormControlLabel,
  useTheme,
} from "@mui/material";
import { Formik, Field } from "formik";
import * as yup from "yup";
import { tokens } from "../../theme";
import Header from "../../components/Header";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const initialValues = {
  algorithm: { language: "python", algorithm: "bubble sort" },
  lowerBound: 1,
  upperBound: 2,
  step: 1,
  repeats: 1,
  arrayTypes: ["random"],
};

const compareSortednessFormSchema = yup.object().shape({
  algorithm: yup.object().shape({
    language: yup.string().required("Select a language"),
    algorithm: yup.string().required("Select an algorithm"),
  }),
  lowerBound: yup
    .number()
    .min(initialValues.lowerBound, "Lower bound must be at least 1")
    .required("Lower bound is required"),
  upperBound: yup
    .number()
    .required("Upper bound is required")
    .test(
      "is-greater",
      "Upper bound must be greater than lower bound",
      function (value) {
        const { lowerBound } = this.parent;
        return value === undefined || value > lowerBound;
      },
    ),
  step: yup
    .number()
    .min(initialValues.step, "Step must be at least 1")
    .required("Step is required")
    .test(
      "step-limit",
      "Step must be less than or equal to upper bound",
      function (value) {
        const { upperBound } = this.parent;
        return upperBound === undefined || value <= upperBound;
      },
    ),
  repeats: yup
    .number()
    .min(initialValues.repeats, "Number of repeats must be at least 1")
    .required("Number of repeats is required"),
  arrayTypes: yup
    .array()
    .of(yup.string())
    .min(initialValues.arrayTypes.length, "Select at least one array type")
    .required("Array types selection is required"),
});

const CompareSortedness = ({ config, setGraphData, setSelected }) => {
  const navigate = useNavigate();
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const transformData = (data = null) => {
    return data["data_series"].map((item) => {
      const arrayType = item["array_type"];

      const dataPoints = item["data"].map(([x, y]) => ({
        x: String(x),
        y: y,
      }));

      return {
        id: arrayType,
        color: colors.greenAccent[100],
        data: dataPoints,
      };
    });
  };

  const handleSubmit = async (values) => {
    const requestBody = {
      algorithm: values.algorithm,
      low: values.lowerBound,
      high: values.upperBound,
      arr_types: values.arrayTypes,
      num_reps: values.repeats,
      step: values.step,
    };

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/compare-sortedness",
        requestBody,
        { timeout: 100000 },
      );

      setGraphData(transformData(response.data));
      setSelected("Graph");
      navigate("/graph");
    } catch (error) {
      console.error("Error:", error);
    }
  };

  const languages = Object.keys(config.algorithms);
  const arrayTypes = config["array types"] || [];

  return (
    <Box m="20px" overflow="hidden">
      <Header
        title="Compare Sortedness"
        subtitle="Configure Sortedness Comparison"
      />

      <Formik
        initialValues={initialValues}
        validationSchema={compareSortednessFormSchema}
        onSubmit={handleSubmit}
      >
        {({
          values,
          errors,
          touched,
          handleChange,
          handleBlur,
          handleSubmit,
        }) => (
          <form onSubmit={handleSubmit}>
            <Box display="grid" gap="20px">
              <TextField
                label="Lower Bound"
                name="lowerBound"
                type="number"
                value={values.lowerBound}
                onChange={handleChange}
                onBlur={handleBlur}
                error={!!touched.lowerBound && !!errors.lowerBound}
                helperText={touched.lowerBound && errors.lowerBound}
              />
              <TextField
                label="Upper Bound"
                name="upperBound"
                type="number"
                value={values.upperBound}
                onChange={handleChange}
                onBlur={handleBlur}
                error={!!touched.upperBound && !!errors.upperBound}
                helperText={touched.upperBound && errors.upperBound}
              />
              <TextField
                label="Step"
                name="step"
                type="number"
                value={values.step}
                onChange={handleChange}
                onBlur={handleBlur}
                error={!!touched.step && !!errors.step}
                helperText={touched.step && errors.step}
              />
              <TextField
                label="Repeats"
                name="repeats"
                type="number"
                value={values.repeats}
                onChange={handleChange}
                onBlur={handleBlur}
                error={!!touched.repeats && !!errors.repeats}
                helperText={touched.repeats && errors.repeats}
              />

              {/* Algorithm Selection */}
              <Box display="flex" gap="20px" alignItems="center">
                <Field
                  as={Select}
                  name="algorithm.language"
                  value={values.algorithm.language}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  error={
                    !!touched.algorithm?.language &&
                    !!errors.algorithm?.language
                  }
                >
                  {languages.map((lang) => (
                    <MenuItem key={lang} value={lang}>
                      {lang}
                    </MenuItem>
                  ))}
                </Field>
                <Field
                  as={Select}
                  name="algorithm.algorithm"
                  value={values.algorithm.algorithm}
                  onChange={handleChange}
                  onBlur={handleBlur}
                  error={
                    !!touched.algorithm?.algorithm &&
                    !!errors.algorithm?.algorithm
                  }
                >
                  {config.algorithms[values.algorithm.language]?.map((algo) => (
                    <MenuItem key={algo} value={algo}>
                      {algo}
                    </MenuItem>
                  ))}
                </Field>
              </Box>

              {/* Array Types */}
              <Box>
                <Box mb={1}>Array Types:</Box>
                {arrayTypes.map((type) => (
                  <FormControlLabel
                    key={type}
                    control={
                      <Checkbox
                        name="arrayTypes"
                        value={type}
                        checked={values.arrayTypes.includes(type)}
                        onChange={(event) => {
                          const selectedArrayTypes = [...values.arrayTypes];
                          if (event.target.checked) {
                            selectedArrayTypes.push(type);
                          } else {
                            const index = selectedArrayTypes.indexOf(type);
                            selectedArrayTypes.splice(index, 1);
                          }
                          handleChange({
                            target: {
                              name: "arrayTypes",
                              value: selectedArrayTypes,
                            },
                          });
                        }}
                      />
                    }
                    label={type}
                  />
                ))}
                {!!touched.arrayTypes && !!errors.arrayTypes && (
                  <Box color="red" fontSize="small">
                    {errors.arrayTypes}
                  </Box>
                )}
              </Box>
            </Box>

            <Button
              type="submit"
              color="primary"
              variant="contained"
              sx={{ mt: 3 }}
            >
              Compare
            </Button>
          </form>
        )}
      </Formik>
    </Box>
  );
};

export default CompareSortedness;
