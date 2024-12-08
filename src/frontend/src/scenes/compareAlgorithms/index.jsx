import React from "react";
import { Box, Button, MenuItem, Select, TextField, useTheme } from "@mui/material";
import { Formik, Field, FieldArray } from "formik";
import { tokens } from "../../theme";
import * as yup from "yup";
import Header from "../../components/Header";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const initialValues = {
  algorithms: [{ language: "python", algorithm: "bubble sort" }],
  lowerBound: 1,
  upperBound: 2,
  step: 1,
  repeats: 1,
  arrayType: "random",
};

const compareAlgorithmsFormSchema = yup.object().shape({
  algorithms: yup
    .array()
    .min(initialValues.algorithms.length, "Select at least one algorithm")
    .required("Algorithm selection is required"),
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
});

const CompareAlgorithms = ({ config, setGraphData, setSelected }) => {
  const navigate = useNavigate();
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  
  const transformData = (data = null) => {
    return data.map((item) => {
      const algorithm = item[0];
      const language = item[1];
      const algorithmId = `${algorithm} (${language})`;

      const dataPoints = item[2].map(([x, y]) => ({
        x: String(x),
        y: y,
      }));

      return {
        id: algorithmId,
        color: colors.greenAccent[100],
        data: dataPoints,
      };
    });
  };

  const handleSubmit = async (values) => {
    const requestBody = {
      algorithms: values.algorithms,
      low: values.lowerBound,
      high: values.upperBound,
      arr_type: values.arrayTypes,
      num_reps: values.repeats,
      step: values.step,
    };

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/compare-algorithms",
        requestBody,
        {timeout: 10000},
      );
      setGraphData(transformData(response.data));
      setSelected("Results");
      navigate("/graph");
    } catch (error) {}
  };

  const languages = Object.keys(config.algorithms);
  const arrayTypes = config["array types"] || [];

  return (
    <Box
      m="20px"
      overflow="hidden"
    >
      <Header
        title="Compare Algorithms"
        subtitle="Configure an Algorithms Comparison"
      />

      <Formik
        initialValues={initialValues}
        validationSchema={compareAlgorithmsFormSchema}
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

              <Field
                as={Select}
                name="arrayType"
                value={values.arrayType}
                onChange={handleChange}
                onBlur={handleBlur}
                error={!!touched.arrayType && !!errors.arrayType}
              >
                {arrayTypes.map((type) => (
                  <MenuItem key={type} value={type}>
                    {type}
                  </MenuItem>
                ))}
              </Field>

              <FieldArray name="algorithms">
                {({ push, remove }) => (
                  <Box>
                    <Button
                      variant="contained"
                      color="primary"
                      onClick={() => push({ language: "", algorithm: "" })}
                    >
                      Add Algorithm
                    </Button>
                    {values.algorithms.map((_, index) => (
                      <Box
                        key={index}
                        display="grid"
                        gridTemplateColumns="1fr 1fr auto"
                        gap="10px"
                        mt={2}
                      >
                        <Field
                          as={Select}
                          name={`algorithms[${index}].language`}
                          value={values.algorithms[index].language}
                          onChange={handleChange}
                          onBlur={handleBlur}
                          error={!!errors.algorithms?.[index]?.language}
                        >
                          {languages.map((lang) => (
                            <MenuItem key={lang} value={lang}>
                              {lang}
                            </MenuItem>
                          ))}
                        </Field>
                        <Field
                          as={Select}
                          name={`algorithms[${index}].algorithm`}
                          value={values.algorithms[index].algorithm}
                          onChange={handleChange}
                          onBlur={handleBlur}
                          error={!!errors.algorithms?.[index]?.algorithm}
                        >
                          {config.algorithms[
                            values.algorithms[index].language
                          ]?.map((algo) => (
                            <MenuItem key={algo} value={algo}>
                              {algo}
                            </MenuItem>
                          ))}
                        </Field>
                        <Button
                          variant="contained"
                          color="secondary"
                          onClick={() => remove(index)}
                        >
                          Remove
                        </Button>
                      </Box>
                    ))}
                  </Box>
                )}
              </FieldArray>
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

export default CompareAlgorithms;
