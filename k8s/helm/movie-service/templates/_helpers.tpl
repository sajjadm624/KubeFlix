{{- define "movie-service.name" -}}
movie-service
{{- end }}

{{- define "movie-service.fullname" -}}
{{ .Release.Name }}-movie-svc
{{- end }}
