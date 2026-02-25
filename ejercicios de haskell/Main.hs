module Main where

import Data.List (intercalate)
import Data.Time (getCurrentTime)
import System.Environment (getArgs)

-- Sintomas conocidos para un mini diagnostico.
data Diagnostico = Diagnostico
  { sintomas :: [String]
  , recomendacion :: String
  } deriving (Show)

recomendar :: [String] -> String
recomendar xs
  | tiene ["fiebre", "dolor"] = "Paracetamol"
  | tiene ["alergia", "estornudos"] = "Loratadina"
  | tiene ["tos", "garganta"] = "Miel y reposo"
  | otherwise = "Observacion y consulta medica"
  where
    tiene req = all (`elem` xs) req

toJson :: Diagnostico -> String
toJson d =
  "{\"sintomas\":[" ++ sintomasJson ++ "],\"recomendacion\":\"" ++ recomendacion d ++ "\"}"
  where
    sintomasJson = intercalate "," (map envolver (sintomas d))
    envolver s = "\"" ++ s ++ "\""

main :: IO ()
main = do
  args <- getArgs
  hora <- getCurrentTime
  let rec = recomendar args
      out = toJson (Diagnostico args rec)
  appendFile "haskell.log" (show hora ++ " | " ++ unwords args ++ " -> " ++ rec ++ "\n")
  putStrLn out
